#!/usr/bin/python3

from sys import stdin
from functools import reduce

t = int(stdin.readline())
for i in range(1, t+1):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    x = reduce(lambda x,y: x^y, a)
    ans = 'NO' if x != 0 else sum(a[1:])
    print('Case #{}: {}'.format(i, ans))
