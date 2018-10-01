#!/usr/bin/env python3
def flip(s):
    return ['-' if c == '+' else '+' for c in s]

def solve(s, k):
    r = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            s[i:i+k] = flip(s[i:i+k])
            r += 1
    return 'IMPOSSIBLE' if '-' in s else r

t = int(input())
for i in range(1, t+1):
    s, k = input().split(' ')
    s = list(s)
    k = int(k)
    print('Case #{}: {}'.format(i, solve(s, k)))
