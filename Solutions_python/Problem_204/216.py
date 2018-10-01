#!/usr/bin/env python3

from collections import deque
import math

def intersects(iterable):
    lowest, highest = iterable[0]
    for low, high in iterable[1:]:
        if high < lowest or low > highest:
            return False
        lowest = max(low, lowest)
        high = min(high, highest)

    return True

def solve(N, P, R, Q):
    #print(f'R = {R}')
    #print(f'Q = {Q}')

    servings = []
    for i in range(N):
        target = R[i]
        least = target * 0.9
        most = target * 1.1

        ingredient_servings = deque()
        for j in range(P):
            least_servings = math.ceil(Q[i][j] / most)
            most_servings = math.floor(Q[i][j] / least)

            if least_servings <= most_servings:
                ingredient_servings.append((least_servings, most_servings))
        servings.append(ingredient_servings)

    #print(servings)

    kits = 0
    while all(map(lambda s: len(s) > 0, servings)):
        candidates = [s[0] for s in servings]
        #print(f'kits = {kits} c = {candidates}')

        if intersects(candidates):
            #print('intersected')
            kits += 1
            for s in servings:
                s.popleft()
        else:
            #print('not intersected')
            low, high = servings[0][0]
            least_max = high
            least_max_index = 0
            for i in range(1, len(servings)):
                low, high = servings[i][0]
                if high < least_max:
                    least_max = high
                    least_max_index = i
            servings[least_max_index].popleft()

    return kits

T = int(input())
for i in range(T):
    N, P = [int(x) for x in input().split(" ")]
    R = [int(x) for x in input().split(" ")]
    Q = []
    for _ in range(N):
        quantities = sorted([int(x) for x in input().split(" ")])
        Q.append(quantities)
    result = solve(N, P, R, Q)
    print(f'Case #{i+1}: {result}')
