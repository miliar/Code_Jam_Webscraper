#!/usr/bin/env pypy3
"""Task #1"""

def solve():
    s1, s2 = input().split()
    state = [True if x == '+' else False for x in s1]
    length = int(s2)

    flips = 0
    while len(state) > length:
        if state[0]:
            state = state[1:]
            continue
        for i in range(length):
            state[i] = not state[i]
        flips += 1
    tail = True
    for i in range(length):
        tail = tail and state[i]
    if tail:
        return flips
    tail = True
    for i in range(length):
        tail = tail and not state[i]
    if tail:
        return flips + 1
    return None

for case in range(1, int(input()) + 1):

    result = solve()
    result = result if result is not None else 'IMPOSSIBLE'

    print('Case #{}: {}'.format(str(case), result))
