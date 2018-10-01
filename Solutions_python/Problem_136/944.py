#!/usr/bin/env python

import sys
import math

T = int(sys.stdin.readline())

for caseno in xrange(T):
    C, F, X = [float(x) for x in sys.stdin.readline().split()]
    
    f = 0
    cspeed = 2.0
    total = 0
    ans = 1e100

    while f < X:
        extra = X / cspeed

       # print "With %d farms, we need %.7f seconds (ans = %.7f)" % (f, total + extra, ans)

        if (total + extra) > ans:
            break

        ans = total + extra
        total += C / cspeed
        # print "%d farms can be acquired in %.7f seconds" % (f, total)

        cspeed += F
        f += 1
        
    print "Case #%d: %.7f" % (caseno + 1, ans)


