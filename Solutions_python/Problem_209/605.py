import os  # NOQA
import sys  # NOQA
import re  # NOQA
import math  # NOQA
from collections import Counter, deque, namedtuple  # NOQA
from itertools import count, product, permutations, combinations, combinations_with_replacement  # NOQA

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD


def surface_area(r, h, r_above=0):
    return (math.pi * r**2) + (2 * math.pi * r * h) - (math.pi * r_above**2)


for case in range(1, int(input()) + 1):
    res = None

    n, k = (int(x) for x in input().split())

    pancakes = []

    for _ in range(n):
        r, h = (int(x) for x in input().split())
        pancakes.append((r, h))

    pancakes.sort()


    best = 0

    for combo in combinations(pancakes, k):
        above = 0
        sa = 0
        for r, h in combo:
            sa += surface_area(r, h, above)
            above = r

        if sa > best:
            best = sa


    print("Case #{}: {}".format(case, best))
