#!/usr/bin/env python
# Approach:
#   1) Determine cost of optimal strategy in which pancakes are reallocated to a
#      maximum of m per plate.
#   2) Maximize (1) over max(P_i) <= 1000 choices of m
import math, sys;
lines = [line for line in sys.stdin];
l = lines[1:];
for T in range(0, int(lines[0])):
    D = int(l[0]);
    P = map(int, l[1].strip().split(' '));
    time = M = max(P);
    for m in range(1, M + 1):
        time = min(time, m + sum([max(int(math.ceil(float(p) / m)) - 1, 0) for p in P]));
    print "Case #%i: %i" % (T + 1, time);
    l = l[2:];
