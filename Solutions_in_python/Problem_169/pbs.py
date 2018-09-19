#!/usr/bin/python

import sys

NCASE = int(sys.stdin.readline())

for case in range(1,NCASE+1):
    line = sys.stdin.readline().split()
    N = int(line[0])
    V,X = map(float, line[1:])
    SRC = [ map(float,sys.stdin.readline().split()) for _ in xrange(N) ]

    print 'Case #%d:' % (case),
    if N == 1:
        if SRC[0][1] == X:
            print '%.9f' % (V/SRC[0][0])
        else:
            print 'IMPOSSIBLE'
    elif N == 2:
        r0, x0 = SRC[0]
        r1, x1 = SRC[1]
        if min(x0,x1) <= X <= max(x0,x1):
            if x0 == x1:
                r0 += r1
                x1 -= 100
            v1 = V*abs(X-x0) / abs(x1-x0)
            v0 = V*abs(X-x1) / abs(x1-x0)
            print '%.9f' % max(v1/r1, v0/r0)
        else:
            print 'IMPOSSIBLE'
    else:
        assert False, "Cannot handle"
