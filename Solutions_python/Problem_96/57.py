#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(N, surprises, p, totals):
    res = 0
    for total in totals:
        cur = [total / 3] * 3
        for i in xrange(total % 3):
            cur[i] += 1
        assert sum(cur) == total
        if cur[0] >= p:
            res += 1
        elif ((p - cur[0]) == 1 and cur[0] == cur[1] and
              cur[0] > 0 and surprises > 0):
            cur[0] += 1
            cur[1] -= 1
            assert all(c >= 0 for c in cur)
            res += 1
            surprises -= 1
    return res

def main():
    for i, line in enumerate(sys.stdin):
        if i == 0:
            continue
        fields = map(int, line.strip().split())
        N = fields[0]
        S = fields[1]
        p = fields[2]
        scores = fields[3:]
        assert len(scores) == N
        print 'Case #{i}: {res}'.format(i=i, res=solve(N, S, p, scores))

if __name__ == '__main__':
    main()
