#!/usr/bin/env python

import math

def generate_square_palindrome_squares(limit):
    sps = []

    for x in xrange(int(math.sqrt(limit))):
        if str(x) == str(x)[::-1]:
            if str(x**2) == str(x**2)[::-1]:
                sps.append(x**2)

    return sps


def run_one(sps, A, B):
    return len([x for x in sps if x <= B]) - len([x for x in sps if x < A])


def run(lines):
    output = []

    sps = generate_square_palindrome_squares(10**14)

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Size of rectangular lawn
        A, B = [int(x) for x in lines.popleft().split()]

        result = run_one(sps, A, B)

        output.append('Case #{0}: {1}'.format(t + 1, result))

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
