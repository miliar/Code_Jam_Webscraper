#!/bin/python

from collections import defaultdict

def split(len_):
    len_ -= 1
    if not len_:
        return []
    elif len_ == 1:
        return [1]
    else:
        a = len_ / 2
        return [a + len_ % 2, a]

def solve(n, k):
    if n == k:
        return [0, 0]

    m = defaultdict(int)
    m[n] += 1

    while True:
        len_, qty = max(m.iteritems(), key = lambda x: x[0])
        if qty >= k:
            r = split(len_)
            while len(r) < 2:
                r += [0]
            return r

        k -= qty
        del m[len_]
        for new_len in split(len_):
            m[new_len] += qty


n = int(raw_input())
for i in xrange(n):
    n, k = map(int, raw_input().split())
    max_, min_ = solve(n, k)
    print 'Case #%d: %d %d' % (i + 1, max_, min_)

