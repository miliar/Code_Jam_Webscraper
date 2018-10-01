#!/usr/bin/env python
from itertools import permutations
import sys

f=open(sys.argv[1])

def read(s=None):
    row = f.next().strip().split()
    if s is None:
        return row
    if len(s) == 1:
        return {'s':str, 'i':int}[s](row[0])
    return tuple({'s':str, 'i':int}[i](j) for i,j in zip(s,row))

def solve2(P,q):
    p=[0]+[1]*P+[0]
    coins = 0
    for r in q:
        p[r]=0
        r1=r+1
        while p[r1]==1:
            coins+=1
            r1+=1
        r1=r-1
        while p[r1]==1:
            coins+=1
            r1-=1
    return coins

def solve():
    P,Q = read('ii')
    q=read('i'*Q)
    if Q==1:
        q=(q,)
    mv = sys.maxint
    for qq in permutations(q):
        mv = min(mv, solve2(P,qq))
    return mv     

def main():
    T=read('i')
    for i in range(1,T+1):
        print "Case #%s: %s"%(i,solve())

if __name__ == "__main__":
    main()
