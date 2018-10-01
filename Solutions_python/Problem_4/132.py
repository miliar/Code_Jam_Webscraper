#!/usr/bin/env python
"""
Google Code Jam: 
"""

from operator import add
 
t = input()
for i in xrange(t):
    n = input()
    xs = [int(d) for d in raw_input().split()]
    ys = [int(d) for d in raw_input().split()]
    out = reduce(add,
                 [x*y for x,y in zip(sorted(xs), sorted(ys, reverse=True))])
    print "Case #%d: %d" % (i+1, out)

    


