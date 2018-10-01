#!/usr/bin/env python

def run_one(mushrooms):
    any_min = 0
    max_eaten = 0

    for idx in range(len(mushrooms)-1):
        diff = mushrooms[idx] - mushrooms[idx+1]
        if diff > 0:
            any_min += diff

        max_eaten = max(max_eaten, diff)

    constant_min = 0

    for idx in range(len(mushrooms)-1):
        constant_min += min(max_eaten, mushrooms[idx])

    return any_min, constant_min


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        N = int(lines.popleft())
        mushrooms = [int(x) for x in lines.popleft().split(' ')]

        any_min, constant_min = run_one(mushrooms)

        output.append('Case #{0}: {1} {2}'.format(t + 1, any_min, constant_min))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
