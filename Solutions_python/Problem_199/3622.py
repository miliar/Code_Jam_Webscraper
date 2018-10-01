from collections import deque
from operator import mul

import sys

file = sys.stdin
# file = open('a.in', "r")

T = int(file.readline())


def all_numbers(iterable):
    for element in iterable:
        if element <= 0:
            return False
    return True


for i, t in enumerate(range(T), 1):
    S, K = file.readline().split()
    K = int(K)
    flipper = [-1 for _ in range(K)] + [1 for _ in range((len(S) - K))]

    pancakes = []
    for s in list(S):
        if s == '+':
            pancakes.append(1)
        else:
            pancakes.append(-1)
    normal = list(reversed(pancakes))
    flipper = deque(flipper)
    result = list(normal)
    y = 0
    rotation_numbers = len(S) - K + 1

    res = None
    for _ in range(rotation_numbers):
        flipper_list = list(flipper)
        if -1 not in result:
            res = 0
            break
        index_r = result.index(-1)
        index_f = flipper_list.index(-1)
        if index_r == index_f:
            result = list(map(mul, result, flipper_list))
            y += 1
        flipper = deque(flipper)
        flipper.rotate(1)
        if all_numbers(result):
            res = y
            break
    if res is None:
        print('Case #{}: IMPOSSIBLE'.format(i))
    else:
        print('Case #{}: {}'.format(i, res))
