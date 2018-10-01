#!/usr/bin/python3

import sys

def flip(l, d, k):
    if d + k > len(l):
        return
    for i in range(d, d + k):
        l[i] = '+' if l[i] == '-' else '-'

def min_moves(s, k):
    s = list(s)
    moves = 0
    for i in range(0, len(s) - k + 1):
        if s[i] != '+':
            flip(s, i, k)
            moves += 1
    for p in s:
        if p == '-':
            return float('inf')
    return moves

n = int(sys.stdin.readline())

for i in range(1, n+1):
    s, k = sys.stdin.readline().split()
    k = int(k)
    ans = min_moves(s, k)
    if ans < float('inf'):
        print('Case #{0}: {1}'.format(i, ans))
    else:
        print('Case #{0}: IMPOSSIBLE'.format(i))
