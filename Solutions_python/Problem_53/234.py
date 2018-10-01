#!/usr/bin/env python
import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    N,K = [int(x) for x in sys.stdin.readline().split()]
    if K % 2**N == 2**N-1:
        print "Case #%d: ON" % (t+1)
    else:
        print "Case #%d: OFF" % (t+1)

