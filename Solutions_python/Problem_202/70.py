#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

#Z = 10**9 + 7
ssr = sys.stdin.readline
ssw = sys.stdout.write
sew = sys.stderr.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())




def max_bipartite_match(E):
    EE = {}
    for x,y in E:
        if x in EE:
            EE[x].append(y)
        else:
            EE[x] = [y]

    UL = set(x for (x,y) in E)
    M = {}
    found = True
    while UL and found:
        found = False
        ULx = list(UL)
        D = set()
        S = []
        while S or ULx:
            #print S
            if not S:
                x = ULx.pop()
                S = [ [x, None, None] ]
                continue
            x = S[-1][0]
            if S[-1][1] == None:
                Q = [ y for y in EE[x] if y not in M ] + \
                    [ y for y in EE[x] if y in M ]
                S[-1][1] = Q
                continue
            if not S[-1][1]:
                S.pop()
                continue
            y = S[-1][1].pop()
            if y in D:
                continue
            D.add(y)
            S[-1][2] = y
            if not y in M:
                found = True
                UL.discard(S[0][0])
                for x,q,y in S:
                    M[y] = x
                break
            S.append([M[y],None,None])

    #assert len(set(M[y] for y in M))==len(y)
    return [ (M[y], y) for y in M ]





def do_one_case(cnum):
    N, M = rdints()
    R = set(range(N))
    C = set(range(N))
    U = set(range(-N+1,N))
    D = set(range(2*N-1))
    G0 = [ N*[0] for i in range(N) ]
    G = [ N*[0] for i in range(N) ]
    B = {"x":1, "+":2, "o":3}
    for i in range(M):
        c, i, j = rdstrs()
        i = int(i)-1
        j = int(j)-1
        c = B[c]
        G[i][j] = G0[i][j] = c
        if c&1:
            R.remove(i)
            C.remove(j)
        if c&2:
            U.remove(i-j)
            D.remove(i+j)
    while(R):
        i = R.pop()
        j = C.pop()
        G[i][j] |= 1
    assert not C
    E = [ (i+j, i-j) for i in range(N) for j in range(N) if i-j in U and i+j in D ]
    #print U
    #print D
    #print E
    M = max_bipartite_match(E)
    #print M
    for s, d in M:
        assert s&1==d&1
        i = (s+d)//2
        j = (s-d)//2
        G[i][j] |= 2
    sp = sum(x&2 for g in G for x in g)
    sp >>= 1
    sp += N
    ch = [ (i, j, G[i][j]) for i in range(N) for j in range(N) if G[i][j]>G0[i][j] ]
    print "Case #%d: %d %d" % (cnum, sp, len(ch))
    BB = [ None, "x", "+", "o" ]
    for i,j,x in ch:
        print "%c %d %d" % (BB[x], i+1, j+1)



def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
