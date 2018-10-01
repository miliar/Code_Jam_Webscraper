#!/usr/bin/env python

import sys
sys.setrecursionlimit(1100)

def allowed(s1, s2):
    colours = [{'R': {'R'}, 'O': {'R', 'Y'}, 'Y': {'Y'}, 'G': {'Y', 'B'}, 'B': {'B'}, 'V': {'B', 'R'}}[s] for s in (s1, s2)]
    return colours[0].isdisjoint(colours[1])

def solve(done, length, left):
    #print(done)
    if len(done) == length:
        return done if allowed(done[0], done[-1]) else 'IMPOSSIBLE'
    for key, value in sorted(left.items(), key=lambda o: o[1])[::-1]:
        if value and (not done or allowed(done[-1], key)):
            l = left.copy()
            l[key] -= 1
            s = solve(done + key, length, l)
            if s != 'IMPOSSIBLE':
                return s
    return 'IMPOSSIBLE'

t = int(input())
for case in range(1, t+1):
    n, r, o, y, g, b, v = [int(s) for s in input().split(' ')]
    if max([r, o, y, g, b, v]) > n/2:
        print(f'Case #{case}: IMPOSSIBLE')
    else:
        print(f'Case #{case}: ' + solve('', n, {'R': r, 'O': o, 'Y': y, 'G': g, 'B': b, 'V': v}))

