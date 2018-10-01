#! /usr/bin/env python3
from collections import deque

UP = '+'
DOWN = '-'
NOWAY = 'IMPOSSIBLE'


def get_negative(cakes):
    negative = []
    for i in cakes:
        if i == UP:
            negative.append(DOWN)
        else:
            negative.append(UP)
    return ''.join(negative)


def count_flips(cakes, capacity):
    cakes_len = len(cakes)
    visited = set()
    to_visit = deque([[cakes, 0]])
    while to_visit:
        cakes, depth = to_visit.popleft()
        if DOWN not in cakes:
            return depth
        if cakes in visited:
            continue
        visited.add(cakes)
        negative = get_negative(cakes)
        for i in range(cakes_len-capacity+1):
            new_cakes = cakes[:i] + negative[i:i+capacity] + cakes[i+capacity:]
            if DOWN not in cakes:
                return depth + 1
            to_visit.append([new_cakes, depth+1])

    return NOWAY

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        cakes, m = input().split(" ")
        capacity = int(m)
        print("Case #{}: {}".format(i + 1, count_flips(cakes, capacity)))
