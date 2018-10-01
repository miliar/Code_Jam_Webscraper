# -*- coding: utf-8 -*-

t = int(raw_input())

for i in xrange(1, t+1):
    c, f, x = [float(e) for e in raw_input().split()]
    res = x / 2.0
    n = 1
    cache = [0.0]
    def b(c, f, n):
        if len(cache) <= n:
            cache.append(cache[-1] + c / (2 + f * n - f))
        return cache[n]
    def g(c, f, n):
        return b(c, f, n) + x / (2 + f * n)
    while g(c, f, n) < res:
        res = g(c, f, n)
        n += 1
    print 'Case #%d:' % i, res
