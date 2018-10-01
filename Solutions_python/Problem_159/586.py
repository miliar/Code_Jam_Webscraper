#!/usr/bin/python3
import numpy as np

t = int(input())


for test_num in range(t):
    _ = int(input())
    m = np.array([int(i) for i in input().split()])

    drop = np.diff(m)
    j = -drop[drop < 0].sum()

    drop_max = np.max(-drop)
    less_than_drop_max = m[:-1][m[:-1] < drop_max]
    k = drop_max * (len(m) - len(less_than_drop_max) - 1) + \
            less_than_drop_max.sum()

    print('Case #{}: {} {}'.format(test_num + 1, j, k))
