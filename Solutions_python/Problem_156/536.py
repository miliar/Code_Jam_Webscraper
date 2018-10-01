#!/usr/bin/python

import sys
sin = sys.stdin
line = lambda : sin.readline().strip()

TEST_CASES = int(line())
for CASE in range(1, TEST_CASES+1):
    D = int(line())
    P = sorted(map(int, line().split(" ")))
    empty_plates = D - len(P)
    D = sum(P)
    for x in range(empty_plates):
        P.append(0)
    P = sorted(P)
    result = P[-1]
    if P[-1] > 3:
        for D in range(1,max(2,max(P))):
            avg = sum(P) / D
            p = P[:]
            p = sorted(p)
            r = 0
            while p[-1] > avg +1:
                p.append(min(avg, p[-1] - avg))
                p[-2] -= p[-1]
                p = sorted(p)
                r += 1
                if r > result:
                    break
            r += p[-1]
            result = min(r, result)
            
    print "Case #%d: %s" % (CASE, result)
