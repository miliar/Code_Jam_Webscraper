#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat Apr 11 12:06:06 2015 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>

import copy
import sys
from multiprocessing import Pool


def do_solve_brute_force(a):
    cache = dict()

    def minius_all(b, c):
        return tuple(v - c for v in b if v - c > 0)

    def search(b):
        if b in cache:
            return cache[b]
        if len(b) == 0:
            return 0
        ret = max(b)
        ret = min(ret, 1 + search(minius_all(b, 1)))

        c = list(b)
        c.sort()
        largest = c.pop()
        for i in xrange(1, largest):
            ret = min(ret, 1 + search(tuple(sorted(c + [i, largest - i]))))

        cache[b] = ret
        return ret

    ans = search(tuple(a))
    return ans


def do_solve(a):
    a = copy.copy(a)
    ans = max(a)
    for i in range(max(a)):
        a.sort()
        largest = a.pop()
        a.append(largest / 2)
        a.append(largest - largest / 2)

        cost = i + 1 + max(a)
        ans = min(ans, cost)
    return ans


def solve(fin):
    lines = [line.rstrip() for line in f]
    n = int(lines[0])
    case_id = 0
    pool = Pool()
    result = []
    for _ in xrange(1, n * 2, 2):
        n = int(lines[_])
        a = map(int, lines[_+1].split())
        result.append(pool.apply_async(do_solve_brute_force, (a,)))
    for i, rst in enumerate(result):
        out = 'Case #{}: {}'.format(i + 1, rst.get())
        print out
        print >> sys.stderr, out



if __name__ == '__main__':
#     conf = [[9]]
#     conf = [[9] * 6]
#     for i in conf:
#         print i
#         ans0 = do_solve_brute_force(i)
#         print i
#         ans1 = do_solve(i)
#         print i, ans0, ans1
#         assert ans0 == ans1, (i, ans0, ans1)

    import sys
    with open(sys.argv[1]) as f:
        solve(f)

# vim: foldmethod=marker
