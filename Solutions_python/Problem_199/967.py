# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import matplotlib.pyplot
import multiprocessing
import numpy
import os
import resource
import scipy
import sys


def solve(P, N):
    PL = len(P)
    f = 0
    for i in range(PL - N + 1):
        if (P[i] == 0):
            f += 1
            for j in range(N):
                P[i + j] ^= 1
    return "IMPOSSIBLE" if (0 in P) else f


def read(F):
     PS, NS = F.readline().split()
     N = int(NS)
     P = ["-+".index(c) for c in PS]
     return [P, N]


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    input_file = "A-large.in"

    # Read cases
    with open(input_file) as F:
        T = int(F.readline())
        cases = [read(F) for case in range(T)]

    # Solve
    def expand_solve(args):
        return solve(*args)
    solutions = multiprocessing.Pool().map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
