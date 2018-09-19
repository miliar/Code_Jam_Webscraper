#!/usr/bin/python3.3

import itertools
import numpy as np
import pprint
import sys


def decide(arr):
    ma = arr.max()
    n, m = arr.shape
    row_mins = list(map(min, arr))
    col_mins = list(map(min, arr.transpose()))
    #print(row_mins, col_mins)
    for i in range(n):
        for j in range(m):
            va = arr[i, j]
            if va == ma:
                continue
            if set(arr[i, np.arange(m)]) == set([va]):
                continue
            if set(arr[np.arange(n), j]) == set([va]):
                continue
            return 'NO'
    return 'YES'


inputs = int(sys.stdin.readline())


for i in range(inputs):
    n, m = map(int, sys.stdin.readline().split())
    raw = []
    for line in itertools.islice(sys.stdin, n):
        raw.extend(map(int, line.split()))
    arr = np.array(raw).reshape(n, m)
    st = decide(arr)
    print('Case #{}: {}'.format(i + 1, st))


