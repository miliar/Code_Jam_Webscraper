# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import multiprocessing
import os
import resource
import sys


def can_make(N, P, R, Q, servings):
    for i in range(N):
        min_servings = Q[i][0] / 1.1 / R[i]
        max_servings = Q[i][0] / 0.9 / R[i]
        if min_servings > servings or max_servings < servings:
            return False
    return True

def solve(N, P, R, Q):
    num = 0
    while min(len(Qi) for Qi in Q) > 0:
        max_possible = min(Q[i][0] / 0.9 / R[i] for i in range(N))
        for servings in range(int(math.ceil(max_possible)) + 1):
            if can_make(N, P, R, Q, servings):
                num += 1
                for i in range(N):
                    Q[i] = Q[i][1:]
                break
        else:
            smallest_index = 0
            for i in range(N):
                if Q[i][0] / 0.9 / R[i] < Q[smallest_index][0] / 0.9 / R[smallest_index]:
                    smallest_index = i

            Q[smallest_index] = Q[smallest_index][1:]
    return num


def read(F):
    N, P = [int(num) for num in F.readline().split()]
    R = [int(num) for num in F.readline().split()]
    Q = [sorted([int(num) for num in F.readline().split()]) for i in range(N)]
    return N, P, R, Q


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    if "--input" in sys.argv and len(sys.argv) >= sys.argv.index("--input"):
        # Use input file from command line
        input_file = sys.argv[sys.argv.index("--input") + 1]
    else:
        sys.exit(1)

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
