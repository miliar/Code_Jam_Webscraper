#!/usr/bin/env python2.6
# -*- Mode: python; indent-tabs-mode: nil; py-indent-offset: 4; python-indent: 4; -*-
# vim:expandtab softtabstop=4 shiftwidth=4:
import sys
from math import log

lg = lambda x: log(x, 2)

def Show(b):
    maxB = max(b)
    maxX = int(lg(maxB+1))
    f = "%%0%dd" %(maxX+1)
    print f
    for v in b:
        print f % int(bin(v)[2:])
def E(vx, vxp):
    vx2 = vx << 1
    c1 = vx & ~(vxp | vx2)
    c2 = ~vx & (vxp & vx2)
    r = vx ^ (
        vx & ~(vxp | vx2)  |
        ~vx & (vxp & vx2)  )
    #print "E:"
    #Show([vxp, vx, c1, c2, r])
    return r
def Iter(b):
    n = 0
    #Show(b)
    while any(b):
        b.append(0)
        bn = b[:]
        for y in range(1, len(b)):
            bn[y] = E(b[y], b[y-1])
        b = bn
        n += 1
        #Show(b)
    return n
def main():
    it = iter(sys.stdin)
    N = int(next(it))
    for i in range(N):
        R = int(next(it))
        b = []
        maxX = 0
        for r in range(R):
            X1, Y1, X2, Y2 = map(int, next(it).split())
            if len(b) <= Y2:
                b.extend([0]*(1+Y2-len(b)))
            maxX = max(maxX, X2)
            m = 2**(1+X2-X1) - 1
            m <<= X1
            for y in range(Y1, Y2+1):
                b[y] |= m
        n = Iter(b)
        print "Case #%d: %d" %(i+1, n)

if __name__=="__main__":
    main()
