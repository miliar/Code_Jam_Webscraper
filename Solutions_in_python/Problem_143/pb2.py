# -*- coding: utf-8 -*-

def solve(a, b, k):
    res = set()
    for i in xrange(a):
        for j in xrange(b):
            if i & j < k:
                res.add((i, j))
    return len(res)

t = int(raw_input())

for i in xrange(1, t+1):
    a, b, k = [int(e) for e in raw_input().split()]
    print 'Case #%d: %d' % (i, solve(a, b, k))
