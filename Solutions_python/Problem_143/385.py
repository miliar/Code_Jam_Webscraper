#!/usr/env/python

import math
from sys import stdin

def solve_prob():
    (A, B, K) = [int(i) for i in stdin.readline().strip().split()]
    c = 0
    for i in range(0, A):
        for j in range (0, B):
            if (i & j) < K:
                c += 1
    return str(c)


nb = int(stdin.readline().strip())
for i in range(1, nb + 1):
    print('Case #{}: {}'.format(i, solve_prob()))
