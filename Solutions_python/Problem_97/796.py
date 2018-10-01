#!/usr/bin/env python

import collections
import sys

from math import log10

def rotations(n):
    return [n[s:] + n[:s] for s in xrange(1, len(n))]

assert '12345' in rotations('34512')
print rotations('34512')

def solve(a, b):
    pairs = set()
    numbers_buckets = collections.defaultdict(set)

    for n in xrange(a, b + 1):
        numbers_buckets[int(log10(n))].add(str(n))

    for bucket, numbers in numbers_buckets.iteritems():
        for n in numbers:
            for candidate in rotations(n):
                if candidate == n:
                    continue

                if candidate in numbers:
                    i_n = int(n)
                    i_c = int(candidate)
                    pairs.add((min(i_n, i_c), max(i_n, i_c)))

    return len(pairs)

if __name__ == "__main__":
    infile = open(sys.argv[1])
    outfile = open('output.txt', 'w')

    no_cases = int(infile.readline())
    for idx, line in enumerate(infile):
        case = idx + 1
        a, b = [int(x) for x in line.split()]
        count = solve(a, b)
        output = "Case #%d: %d\n" % (case, count)
        print output
        outfile.write(output)

