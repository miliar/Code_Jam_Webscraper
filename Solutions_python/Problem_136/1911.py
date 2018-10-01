#!/usr/bin/env python

def run_one(C, F, X):
    time = 0
    rate = 2.0

    while True:
        time_to_factory = C / rate
        time_with_factory = time_to_factory + X / (rate + F)
        time_without_factory = X / rate

        if time_with_factory < time_without_factory:
            time += time_to_factory
            rate += F
        else:
            time += time_without_factory
            break

    return time


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        C, F, X = [float(x) for x in lines.popleft().split()]

        result = run_one(C, F, X)

        output.append('Case #{0}: {1:.7f}'.format(t + 1, result))

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
