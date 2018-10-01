#!/usr/bin/env python

from __future__ import division

import sys
import math

f=open(sys.argv[1])

def read(s=None):
    row = f.next().strip().split()
    def int_or_str(s):
        try:
            return int(s)
        except:
            return s

    if s is None:
        return map(int, row)

    if len(s) == 1:
        return {'s':str, 'i':int}[s](row[0])
    return tuple({'s':str, 'i':int}[i](j) for i,j in zip(s,row))

def solve():
    N=read('i')
    P=[read() for i in range(N)]
    mv=sys.maxint
    if N==1:
        return P[0][2]
    if N==2:
        return max(P[0][2], P[1][2])
    for i in range(N-1):
        for j in range(i+1,N):
            ix,iy,ir = P[i]
            jx,jy,jr = P[j]
            d=math.sqrt((ix-jx)**2+(iy-jy)**2)+ir+jr
            if d<mv:
                mv=d
                mi=i
                mj=j
                R=d/2

    for k in range(N):
        if k!=mi and k !=mj:
            break

    return max(R,P[k][2])

         
def main():
    T=read('i')
    for i in range(1,T+1):
        print "Case #%s: %s"%(i,solve())

if __name__ == "__main__":
    main()
