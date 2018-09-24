#!/usr/bin/env python

import sys

testcases = int(sys.stdin.readline())
for t in range(1, testcases + 1):
    se = {}
    switchcount = 0
    searchengines = int(sys.stdin.readline())
    while searchengines > 0:
        se[sys.stdin.readline().strip()] = 0
        searchengines -= 1
    queries = int(sys.stdin.readline())
    while queries > 0:
        query = sys.stdin.readline().strip()
        se[query] += 1
        if 0 not in se.values():
            switchcount += 1
            for k in se.keys():
                se[k] = 0
            se[query] += 1
        queries -= 1
    print 'Case #%d: %d' % (t, switchcount)
