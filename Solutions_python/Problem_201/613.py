from sys import stdin
from math import floor, ceil
import heapq
import bisect
from collections import defaultdict

T = int(stdin.readline())

def update(parts, elem, count):
    if not parts:
        parts.append((elem, count))
    else:
        index = bisect.bisect_left(parts, (elem, count))

        if index < len(parts) and parts[index][0] == elem:
            parts[index] = (parts[index][0], parts[index][1] + count)
        else:
            parts[index:index] = [(elem, count)]

for case in range(1, T+1):
    (N, K) = stdin.readline().split()
    (N, K) = (int(N), int(K))

    parts = [(N, 1)]

    moves = 0
    done = False

    while not done:
        (choice, count) = parts.pop()
        remaining = choice - 1
        m = remaining // 2
        M = m + (remaining % 2)

        if moves + count >= K:
            done = True
        else:
            update(parts, m, count)
            update(parts, M, count)

            moves += count

    print("Case #{}: {} {}".format(case, M, m))