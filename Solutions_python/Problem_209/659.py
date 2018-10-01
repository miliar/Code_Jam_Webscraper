#!/usr/bin/env python3

from collections import namedtuple
from itertools import combinations
from math import pi

Area = namedtuple('Area', 'side top')

def exposed_area(stack):
    return stack[0].top + sum(pancake.side for pancake in stack)

t = int(input())
for i in range(1, t + 1):
    print('Case #{}: '.format(i), end='')
    n, k = map(int, input().split())
    pancakes = []
    for j in range(n):
        r, h = map(int, input().split())
        pancakes.append(Area(side=2 * pi * r * h, top=pi * r * r))
    pancakes.sort(key=lambda p: p.top, reverse=True)
    best = max(exposed_area(stack) for stack in combinations(pancakes, k))
    print(best)
