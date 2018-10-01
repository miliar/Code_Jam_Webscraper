# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import multiprocessing
import os
import resource
import sys

def product(I):
    p = 1
    for i in I:
        p *= i
    return p


def solve(N, K, U, P):
    P.sort()
    s = 0
    for i in range(len(P)):
        s += P[i]
        if (i + 1) * P[i] - s >= U:
            s -= P[i]
            i -= 1
            break
    if i >= 0:
        AF = (U + s) / (i + 1)

        for j in range(i + 1):
            P[j] = AF

    return product(P)


def read(F):
    N, K = [int(num) for num in F.readline().split()]
    [U] = [float(num) for num in F.readline().split()]
    P = [float(num) for num in F.readline().split()]
    return N, K, U, P


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    if "--input" in sys.argv and len(sys.argv) >= sys.argv.index("--input"):
        # Use input file from command line args
        input_file = sys.argv[sys.argv.index("--input") + 1]
    else:
        # Find the most recently downloaded input file
        input_files = [name for name in os.listdir(".") if name.endswith(".in")]
        input_file = max(input_files, key = os.path.getmtime)

    # Read cases
    with open(input_file) as F:
        T = int(F.readline())
        cases = [read(F) for case in range(T)]

    # Solve
    def expand_solve(args): return solve(*args)

    solutions = multiprocessing.Pool().map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
