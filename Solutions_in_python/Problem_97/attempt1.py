#!/usr/bin/env python
from sys import stdin
from itertools import permutations

def recycle(a):
    sa = str(a)
    la = len(sa)
    for i in xrange(1, la):
        yield int(sa[-i:] + sa[:la-i])

numtests = int(stdin.readline())
for tn in xrange(0, numtests):
    n,m = map(lambda n: int(n), stdin.readline().split())

    count = 0
    for i in xrange(n,m+1):
        last_r = None
        for r in recycle(i):
            if r >= n and r <= m and r > i and r != last_r:
                count += 1
                last_r = r
                #print (i,r)
    print "Case #%d: %d" % (tn+1, count)

# vim:set expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap:



