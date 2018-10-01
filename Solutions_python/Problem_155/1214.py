#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())
for i in range(0,t):
    (smaxs, sstring) = sys.stdin.readline().split(' ')
    smax = int(smaxs)
    slist = list(sstring)
    needed = 0
    total = 0
    for k in range(0, smax+1):
        if (int(slist[k]) > 0) and (total + needed < k):
            needed = k - total
        total = total + int(slist[k])
    print "Case #" + str(i+1) + ": " + str(needed)
