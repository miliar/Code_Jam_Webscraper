#!/usr/bin/python

import sys


def ReadN(fp):
    return int(fp.readline().strip())

def ReadSize(fp):
    return [int(it) for it in fp.readline().strip().split()]

def ReadLawn(fp,N,M):
    lawn = []
    for i in xrange(N):
        tL = [int(t) for t in fp.readline().strip().split()]
        lawn.append(tL)
    return lawn


def CheckColMust(lawn,i, m):
    a = m
    for t in xrange(1,len(lawn)):
        if a<lawn[t][i]:
            return False
    return True
            
def CheckRowMust(lawn,i, m):
    a = m
    for t in xrange(1,len(lawn[0])):
        if a<lawn[i][t]:
            return False
    return True

def CheckLawn(lawn):
    # h line
    for tL in lawn:
        a = max(tL)
        for i,t in enumerate(tL):
            if t<a:
                if not CheckColMust(lawn, i, t):
                    return False
    # v line
    for vt in xrange(len(lawn[0])):
        col = [s[vt] for s in lawn]
        a = max(col)
        for i,t in enumerate(col):
            if t<a:
                if not CheckRowMust(lawn,i, t):
                    return False
    return True


def Test(fname):
    fp = open(fname)
    res = open(fname[:-3]+"_res.txt","wt")
    T = ReadN(fp)
    for i in xrange(T):
        N, M = ReadSize(fp)
#        print N,M
        lawn = ReadLawn(fp,N,M)
#        print lawn
        ok = CheckLawn(lawn)
        ans = ""
        if ok:
            ans = "Case #%d: YES\n" %(i+1)
        else:
            ans = "Case #%d: NO\n" %(i+1)
        res.write(ans)

    fp.close()
    res.close()
    print "done."


if __name__=="__main__":
    if len(sys.argv)<2:
        print "please give input file"
        sys.exit()
    fname = sys.argv[1]
    Test(fname)

