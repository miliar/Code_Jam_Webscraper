import sys
from math import *
from copy import copy, deepcopy
from itertools import product, permutations, combinations
from Queue import Queue


sys.setrecursionlimit(1500)


for test in range(1, int(raw_input()) + 1):

    D, N = map(int, raw_input().split())
    horses = [map(float, raw_input().split()) for _ in range(N)]
    D = float(D)

    horses.sort()
    times = [float('inf')] * N
    max_speed = [float('inf')] * N

    for i in range(N - 1, -1, -1):
        _d = D - horses[i][0]
        _t = _d / horses[i][1]

        #print _d, _t

        times[i] = _t
        max_speed[i] = horses[i][1]

        for j in range(i + 1, N):
            max_speed[i] = min(max_speed[i], _d / times[j])
            times[i] = _d / max_speed[i]

    #print max_speed
    answer = D / times[0]

    print 'Case #{}: {:.6f}'.format(test, answer)
