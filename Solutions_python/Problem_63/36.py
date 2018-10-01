#!/usr/bin/python

from math import log, ceil

T = int(raw_input())

for i in range(T):
    L, P, C = (float(s) for s in raw_input().split(' '))
    n = ceil(log(ceil(log(P/L, C)), 2))
    print "Case #%i: %i" % (i+1, n)
