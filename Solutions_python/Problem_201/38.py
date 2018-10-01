#!/usr/bin/env python2
import heapq
def lsrs(n):
    assert n > 0
    lsrs = n - 1
    ls = lsrs / 2
    rs = lsrs - (lsrs / 2)
    return ls, rs
def score(n):
    assert n > 0
    return -n
def split(n, m):
    assert n >= 0
    if n == 0:
        return []
    lsrs = n - 1
    ls = lsrs / 2
    rs = lsrs - (lsrs / 2)
    ret = []
    assert ls <= rs
    if ls > 0:
        ret += [(score(ls), ls, m)]
    if rs > 0:
        ret += [(score(rs), rs, m)]
    return ret
def compact_pop(q):
    (score1, cn1, m1) = heapq.heappop(q)
    while True:
        if not q:
            break
        c2 = heapq.heappop(q)
        (score2, cn2, m2) = c2
        if cn1 == cn2:
            assert score1 == score2
            m1 += m2
        else:
            heapq.heappush(q, c2)
            break
    return (score1, cn1, m1)
def solve(n, k):
    q = [(score(n), n, 1)]
    ret = None
    sum_m = 0
    while True:
        assert sum(_[1] * _[2] for _ in q) + sum_m == n
        (_, cn, m) = compact_pop(q)
        #(_, cn, m) = heapq.heappop(q)
        sum_m += m
        k -= m
        if k <= 0:
            break
        for next_c in split(cn, m):
            heapq.heappush(q, next_c)
        assert sum(_[1] * _[2] for _ in q) + sum_m == n
    return lsrs(cn)
for t in xrange(1, 1 + int(raw_input())):
    print 'Case #%d:' % t,
    n, k = map(int, raw_input().split())
    ls, rs = solve(n, k)
    print rs, ls
