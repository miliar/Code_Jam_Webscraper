# Written by Nikolai Artemiev

import collections
import functools
import itertools
from math import ceil, floor
import matplotlib.pyplot
import multiprocessing
import numpy
import os
import resource
import scipy
import sys

def add_to_set(s, key, num):
    if key not in s:
        s[key] = 0
    s[key] += num


def solve(N, K):
    blocks = { N: 1 }

    while K > 0:
        biggest = max(blocks.keys())
        num_blocks = blocks[biggest]

        split_size = (biggest - 1) / 2.0
        if num_blocks >= K:
            return "{} {}".format(ceil(split_size), floor(split_size))
        else:
            del blocks[biggest]
            K -= num_blocks
            add_to_set(blocks, ceil(split_size), num_blocks)
            add_to_set(blocks, floor(split_size), num_blocks)



def read(F):
    return [int(num) for num in F.readline().split()]


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    input_file = "C-small-2-attempt0.in"

    # Read cases
    with open(input_file) as F:
        T = int(F.readline())
        cases = [read(F) for case in range(T)]

    # Solve
    def expand_solve(args):
        return solve(*args)
    solutions = multiprocessing.Pool(1).map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
