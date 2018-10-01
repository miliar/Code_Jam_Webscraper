#!/usr/bin/env python

T = int(raw_input())
for case in xrange(1,T+1):
    C, F, X = [float(x) for x in raw_input().split()]

    t = 0
    cookies = 0

    while True:
        rate = 2.0 + cookies*F
        delay = C / rate
        next_rate = 2.0 + (cookies+1)*F
        if delay + X/next_rate > X/rate:
            break
        t += delay
        cookies += 1
    t += X/rate
    print "Case #%d: %.7f" % (case, t)
