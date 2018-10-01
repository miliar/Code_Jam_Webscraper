#!/usr/bin/env python

import sys

with open(sys.argv[1]) as infile:
    cases = [[int(item) for item in line.split()] for line in infile][1:];
    cid = 0;
    for case in cases:
        cid += 1;
        N = case[0];
        S = case[1];
        p = case[2];
        T = case[3:];
        good = 0;
        kick = 0;
        for i in range(N):
            if (p * 3 - 2 <= T[i]):
                good += 1;
            elif (p > 1 and p * 3 -4 <= T[i]):
                kick += 1;
        print "Case #%d: %d" % (cid, good + min(kick, S));
