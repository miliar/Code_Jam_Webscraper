#!/usr/bin/env python2.6
N = 1000L
C = 100
T = long(10**50)
print C
for c in xrange(C):
    print N,
    for n in xrange(N):
        print abs(T - 2**n),
    print
