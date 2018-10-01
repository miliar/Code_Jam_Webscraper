#!/usr/bin/env python3
# coding: utf-8

def solve():
    n = 0
    while (C - X) / (2 + n * F) < -X / (2 + (n + 1) * F):
        n += 1

    ans = 0
    for i in range(n):
        ans += C / (2 + i * F)
    ans += X / (2 + n * F)

    return ans

for case in range(int(input())):
    C, F, X = map(float, input().split(' '))
    print('Case #{}: {:.7f}'.format(case + 1, solve()))
