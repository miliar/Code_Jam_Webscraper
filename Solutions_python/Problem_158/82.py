#
# Compiled with cython v0.22 using --embed option
#

import sys, os, re, string, math, fractions, itertools
from fractions import Fraction

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())

ominoes = {}
rich = set()
gabe = set()
dq = ((0,1), (1,0), (0,-1), (-1,0))


def find_ominoes(X):
    if X in ominoes:
        return ominoes[X]
    Z = find_ominoes2(X)
    ominoes[X] = Z
    return Z


def find_ominoes2(X):
    assert X>1
    SS = set()
    S = set([(0,0)])
    L = [ (0,0), [(0,1), (1,0)] ]
    while(L):
        if not L[-1]:
            L.pop()
            S.remove(L.pop())
            continue
        p = L[-1].pop()
        S.add(p)
        if len(L)==2*X-2:
            fs = frozenset(S)
            SS.add(fs)
            S.remove(p)
            continue
        L.append(p)
        l = set()
        (i,j) = p
        for (di,dj) in dq:
            ii = i+di
            jj = j+dj
            pp = (ii,jj)
            if ii>=0 and (ii>0 or jj>0):
                l.add(pp)
        for i in L[1::2]:
            l.update(i)
        L.append(sorted(pp for pp in l if pp not in S))


    # de-dup
    L = []
    nn = len(SS)
    while(SS):
        l = sorted(SS.pop())
        S = set()
        for a in range(2):
            for b in range(4):
                ii = min(i for (i,j) in l)
                jj = min(j for (i,j) in l if i==ii)
                fs = frozenset((i-ii, j-jj) for (i,j) in l)
                if fs not in S:
                    S.add(fs)
                    if (a,b)!=(0,0):
                        SS.remove(fs)
                l = [ (j,-i) for (i,j) in l ]
            l = [ (j,i) for (i,j) in l ]
        L.append(list(S))
                
    if False:
        print "%d oriented %d-ominoes (%d families):" % (nn, X, len(L))
        for l in L:
            fs = l[0]
            print ""
            print len(l), "versions of:"
            r = 1 + max(i for (i,j) in fs)
            A = [ (2*X+1)*[" "] for i in range(r)]
            for (i,j) in fs:
                A[i][X+j] = "*"
            for i in A:
                print " ".join(i)

    O = []
    OF = []
    OD = {}
    for i in range(len(L)):
        l = L[i]
        for fs in l:
            fst = tuple(sorted(fs))
            OD[fst] = len(O)
            O.append(fst)
            OF.append(i)
    return (O, OF, OD)


cdef:
    struct Placed:
        int i, j, t
    struct Rel:
        int ii, jj

def solve_one_interesting_case(int X, R, C):
    cdef:
        int h, i, j, k, ii, jj, kk, k3, i0, j0
        unsigned long Sc, Scall
        Placed Lc[400]
        unsigned char A[20][32]
        bint flag
        int OFc[1000]
        Rel Oc[1000][6]
        Rel e0[6]

    assert X<=6
    (O, OF, OD) = find_ominoes(X)
    no = len(O)
    assert no<1000
    for i in range(no):
        for j in range(X):
            Oc[i][j].ii, Oc[i][j].jj = O[i][j]
        OFc[i] = OF[i]
    nof = len(set(OF))
    assert nof<64
    N = R*C // X
    assert N*X == R*C
    assert N>1
    h = 0
    Lc[0].i = 0
    Lc[0].j = 0
    Lc[0].t = -1
    S = set()
    Sc = 0
    Scall = ((<unsigned long>1)<<nof)-1
    #A = [ C*[False] for i in range(R) ]
    for ii in range(R):
        for jj in range(C):
            A[ii][jj] = 0
    while h>=0:
        Lc[h].t += 1
        i = Lc[h].i
        j = Lc[h].j
        k = Lc[h].t
        if k>=no:
            h -= 1
            if h>=0:
                i = Lc[h].i
                j = Lc[h].j
                k = Lc[h].t
                #l = O[k]
                #for (ii,jj) in l:
                #    A[i+ii][j+jj] = 0
                for l in range(X):
                    ii = Oc[k][l].ii
                    jj = Oc[k][l].jj
                    A[i+ii][j+jj] = 0
            continue
        #l = O[k]
        #if any(i+ii>=R or j+jj>=C or j+jj<0 or A[i+ii][j+jj] for (ii,jj) in l):
        #    continue
        #for (ii, jj) in l:
        #    A[i+ii][j+jj] = 1
        flag = False
        for l in range(X):
            ii = Oc[k][l].ii
            jj = Oc[k][l].jj
            if i+ii>=R or j+jj>=C or j+jj<0 or A[i+ii][j+jj]:
                flag = True
                break
        if flag:
            continue
        for l in range(X):
            ii = Oc[k][l].ii
            jj = Oc[k][l].jj
            A[i+ii][j+jj] = 1

        if h+2==N:
            #e = [ (ii,jj) for ii in range(R) for jj in range(C) if not A[ii][jj] ]
            #i0 = min(ii for (ii,jj) in e)
            #j0 = min(jj for (ii,jj) in e if ii==i0)
            #e = tuple((ii-i0,jj-j0) for (ii,jj) in e)
            kk = 0
            for ii in range(i,R):
                for jj in range(C):
                    if not A[ii][jj]:
                        assert kk<X
                        e0[kk].ii = ii
                        e0[kk].jj = jj
                        kk += 1
            assert kk==X
            i0 = e0[0].ii
            j0 = e0[0].jj
            e = tuple((e0[kk].ii-i0,e0[kk].jj-j0) for kk in range(X))
            if e in OD:
                kk = OD[e]
                jj = OFc[kk]
                #S.add(jj)
                Sc |= (<unsigned long>1)<<jj
                for ii in range(h+1):
                    jj = OFc[Lc[ii].t]
                    #S.add(jj)
                    Sc |= (<unsigned long>1)<<jj
                #if len(S)==nof:
                if Sc == Scall:
                    return "GABRIEL"
            #for (ii, jj) in l:
            #    A[i+ii][j+jj] = 0
            for l in range(X):
                ii = Oc[k][l].ii
                jj = Oc[k][l].jj
                A[i+ii][j+jj] = 0
            continue
        else:
            #i0 = min(ii for ii in range(R) if not all(A[ii]))
            #j0 = min(jj for jj in range(C) if not A[i][jj])
            i0 = R
            j0 = C
            for jj in range(j+1, C):
                if not A[i][jj]:
                    i0 = i
                    j0 = jj
                    break
            for ii in range(i+1, R):
                if i0<R:
                    break
                for jj in range(C):
                    if not A[ii][jj]:
                        i0 = ii
                        j0 = jj
                        break
            h += 1
            Lc[h].i = i0
            Lc[h].j = j0
            Lc[h].t = -1
    #if len(S)<nof:
    if Sc < Scall:
        return "RICHARD"
    else:
        return "GABRIEL"
    #return "UNCLEAR"



def do_one_case(cnum):
    (X, R, C) = rdints()
    ans = solve_one_case(X, R, C)
    print "Case #%d: %s" % (cnum, ans)


def solve_one_case(X, R, C):
    if C>R:
        (R,C) = (C,R)
    if (X,R,C) in rich:
        return "RICHARD"
    if (X,R,C) in gabe:
        return "GABRIEL"
    ans = solve_one_case2(X, R, C)
    if ans=="RICHARD":
        rich.add((X, R, C))
        rich.add((X, C, R))
    elif ans=="GABRIEL":
        gabe.add((X, R, C))
        gabe.add((X, C, R))
    return ans


def solve_one_case2(X, R, C):
    if C>R:
        (R,C) = (C,R)
    if X>=7:
        return "RICHARD"
    if (R*C)%X:
        return "RICHARD"
    if C < (X+1)//2:
        return "RICHARD"
    if R < X:
        return "RICHARD"
    if X<=2:
        return "GABRIEL"    # X==1 or X==2 and R*C even

    if False and X==6 and C==3:
        return "RICHARD"    # seems to be a pattern for now...

    for i in range(1,R):
        if (X, i, C) in gabe and (X, R-i, C) in gabe:
            return "GABRIEL"
    for i in range(1,C):
        if (X, R, i) in gabe and (X, R, C-i) in gabe:
            return "GABRIEL"
    sys.stdout.flush()
    return solve_one_interesting_case(X, R, C)


def load_precomputed_cases():
    if os.path.exists("precomputed"):
        for x in file("precomputed"):
            v = x.strip().split()
            assert len(v)==4
            X, R, C = map(int, v[:3])
            if v[3]=="RICHARD":
                rich.add((X, R, C))
                rich.add((X, C, R))
            elif v[3]=="GABRIEL":
                gabe.add((X, R, C))
                gabe.add((X, C, R))
    
    

def main():
    if len(sys.argv)>1 and sys.argv[1]=="precompute":
        for X in range(1,7):
            for R in range(1,21):
                for C in range(1,21):
                    print X, R, C, solve_one_case(X,R,C)
        return
    load_precomputed_cases()
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
