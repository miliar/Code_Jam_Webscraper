#!/usr/bin/python2
### Google Code Jam template
# Futures
from __future__ import division
from __future__ import with_statement
from __future__ import print_function

from collections import Counter

## Library
# @memoized
def memoized(func):
    mem = {}

    def wrapped(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapped

## Input templates
# Line as int
readint = lambda infile: int(infile.readline())
# Line as many ints
readints = lambda infile: [int(s) for s in infile.readline().split()]


# Base class
class ProblemSolver(object):
    def __init__(self):
        self.precalculate()

    def precalculate(self):
        raise NotImplementedError

    def process(self, infile, ncase):
        raise NotImplementedError

    def run(self, infile, outfile):
        cases = int(infile.readline())
        for ncase in range(cases):
            print("Case #{nc}".format(nc=ncase + 1))
            # Perform all nessesary calculation
            data = self.process(infile, ncase=ncase)
            outfile.write("Case #{nc}: {data}\n".format(
                nc=ncase + 1, data=data))


# Working class
class Solver(ProblemSolver):
    def precalculate(self):
        ## User code here
        pass

    def process(self, infile, ncase):
        ## User code here
        _, size = readints(infile)
        groups = [g % size for g in readints(infile)]
        group_counts = Counter(groups)
        total = group_counts[0] # Whole groups go ahead
        group_counts[0] = 0
        if size == 2:
            total += (group_counts[1] + 1) // 2
        elif size == 3:
            total += min(group_counts[1], group_counts[2])
            leftover = max(group_counts[1], group_counts[2]) - min(group_counts[1], group_counts[2])
            total += (leftover + 2) // 3
        elif size == 4:
            num_pairs = group_counts[2] // 2
            total += num_pairs
            group_counts[2] -= num_pairs * 2 # maybe one left over
            left_2 = group_counts[2]
            num_pairs = min(group_counts[1], group_counts[3])
            total += num_pairs
            leftovers = max(group_counts[1], group_counts[3]) - num_pairs
            if left_2:
                leftovers += 2
            total += (leftovers + 3) // 4
        return total

# Script code
if __name__ == '__main__':
    ## Setup
    # Task letter
    from os.path import basename, splitext
    TASK = splitext(basename(__file__))[0]
    print("Task {}".format(TASK))
    from sys import argv
    if len(argv) > 1:
        print("Filename given: {}".format(argv[1]))
        FILE = splitext(argv[1])[0]
    else:
        FILE = TASK
    ## Precalculation
    print("Initialization...")
    solver = Solver()
    print("Initialization done.")
    ## Calculation
    print("Calculation...")
    with open(FILE + ".in") as infile:
        with open(FILE + ".out", mode="wt") as outfile:
            solver.run(infile, outfile)
    print("Calculation done.")
