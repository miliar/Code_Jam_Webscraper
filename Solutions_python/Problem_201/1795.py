#!/usr/bin/python
# coding: utf8

"""
    Google Code Jam 2017 - Qualification round
    Problem D
"""

from sys import stdin


def _update_set(row, s, i):
    n = len(row)
    for j in range(i - 1, -1, -1):
        s[j][1] = i - j - 1
        if row[j] == 1:
            break
    for j in range(i + 1, n):
        s[j][0] = j - i - 1
        if row[j] == 1:
            break
    return s


def _choose(row, s):
    min_stall = [(min(s[i]), i) if row[i] == 0 else (-1, -1) for i in range(len(s))]
    best, j = max(min_stall, key=lambda v: v[0])
    candidates = []
    for k in range(len(s)):
        if min_stall[k][0] == best:
            candidates.append(k)
    #print('Candidates : %s' % candidates)
    if len(candidates) > 1:
        max_stall = [(max(s[i]), i) if row[i] == 0 and i in candidates else (-1, -1) for i in range(len(s))]
        #print('Max : %s' % max_stall)
        best, j = max(max_stall, key=lambda v: v[0])
    return best, j


def solve():
    dataset = stdin.readline().split()
    n = int(dataset[0])
    k = int(dataset[1])
    row = [0] * n
    s = []
    for i in range(n):
        s.append([i, n - 1 - i])
    for i in range(k - 1):
        #print('Row : %s' % row)
        #print('Set : %s' % s)
        _,  j = _choose(row, s)
        s = _update_set(row, s, j)
        row[j] = 1
        #print('------')
    #print('Row : %s' % row)
    #print('Set : %s' % s)
    _,  j = _choose(row, s)
    return max(s[j]), min(s[j])

if __name__ == '__main__':
    n = int(stdin.readline())
    for i in range(n):
        y, z = solve()
        print('Case #%i: %i %i' % (i + 1, y, z))
