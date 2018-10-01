#!/usr/bin/env python

from sys import stdin
from math import ceil

C = int(stdin.readline())

def timeto(goal,pos,speed):
    return int(ceil((goal-pos)/float(speed)))

for CASO in xrange(1,C+1):
    (N, K, B, T) = [int(x) for x in stdin.readline().strip().split(" ")]
    X = [int(x) for x in stdin.readline().strip().split(" ")]
    V = [int(x) for x in stdin.readline().strip().split(" ")]

    all = zip(X,V)
    can = [i for (i, (pos,speed)) in enumerate(all) if timeto(B,pos,speed) <= T]
    cant = [i for (i, (pos,speed)) in enumerate(all) if timeto(B,pos,speed) > T]

    if len(can) < K:
        print "Case #%d: IMPOSSIBLE" % (CASO)
        continue

    reached = 0
    swaps = 0
    swap_incr = 0

    for i in xrange(len(all)-1,-1,-1):
        if i in cant:
            swap_incr += 1
        else:
            swaps += swap_incr
            reached += 1

        if reached == K:
            break

    print "Case #%d: %d" % (CASO, swaps)
