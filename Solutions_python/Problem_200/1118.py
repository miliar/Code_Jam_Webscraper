#!/usr/bin/env python3
def is_tidy(n):
    s = list(str(n))
    return s == sorted(s)
def solve(n):
    while not is_tidy(n):
        n -= 1
    return n
t = int(input())
for x in range(t):
    n = int(input())
    print('Case #{}: {}'.format(x+1, solve(n)))

