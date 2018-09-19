#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: solve.large.py
# $Date: Sun May 10 19:54:39 2015 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>


import sys
from collections import Counter
from itertools import product


def bananas_to_bring(target, S):
    assert len(target) <= S
    ret = 0
    s = ''
    for i in range(S - len(target) + 1):
        if i < len(s):
            if s[i:] == target[:len(s) - i]:
                s = s[:i] + target
                ret += 1
        else:
            s += target
            ret += 1
    return ret


def number_of_appearance(a, s):
    ret = 0
    pos = 0
    while True:
        pos = s.find(a, pos)
        if pos == -1:
            return ret
        ret += 1
        pos += 1


def solve(fin):
    K, L, S = map(int, fin.readline().rstrip().split())
    keyboard = fin.readline().rstrip()
    target = fin.readline().rstrip()
    return solve_large(K, L, S, keyboard, target)
    return solve_bf(K, L, S, keyboard, target)


def solve_bf(K, L, S, keyboard, target):

    if set(keyboard) & set(target) != set(target):
        return 0

    b = bananas_to_bring(target, S)
    count = 0
    for perm in product(keyboard, repeat=S):
        c = number_of_appearance(target, ''.join(perm))
#         print target, c, perm
        count += b - c

    return count / float(len(keyboard) ** S)


_cache = dict()
def get_next_j(target, prefix_len, next_char):
    key = (target, prefix_len, next_char)
    if key in _cache:
        return _cache[key]

    s = target[:prefix_len] + next_char
    if prefix_len == len(target):
        start = 1
    else:
        start = 0

    for i in xrange(start, len(s)):
        if s[i:] == target[:len(s) - i]:
            return len(s) - i

    return 0


def solve_large(K, L, S, keyboard, target):

    if set(keyboard) & set(target) != set(target):
        return 0

    b = bananas_to_bring(target, S)

    # f[i,j], i: in a prefix of length i
    #         j: a suffix of length j is the same as a prefix of target
    #         value: the expected number of bananas will be kept


    cnt = [
        [
            0 for j in xrange(L + 1)
        ] for i in xrange(S + 2)
    ]

    f = [
        [
            0 for j in xrange(L + 1)
        ] for i in xrange(S + 2)
    ]


    cnt[0][0] = 1
    for i in xrange(0, S + 1):
        for j in xrange(0, L + 1):
            if i < j:
                continue
            val = f[i][j]

            for ch in keyboard:
                next_j = get_next_j(target, j, ch)
                f[i+1][next_j] += val + (next_j == L) * cnt[i][j]
                cnt[i+1][next_j] += cnt[i][j]

    ans = float(sum(f[S])) / len(keyboard) ** S

    return b - ans


def main():
    fin = sys.stdin
#     fin = open('input')

    T = int(fin.readline().rstrip())
    for case_id in xrange(1, T + 1):
        print >> sys.stderr, 'processing {}'.format(case_id)
        print 'Case #{}: {}'.format(case_id, solve(fin))


if __name__ == '__main__':
    main()

# vim: foldmethod=marker
