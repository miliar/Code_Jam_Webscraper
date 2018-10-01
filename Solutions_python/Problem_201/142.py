#!/usr/bin/python

from collections import OrderedDict
import sys


def split(seq_size):
    half = (seq_size - 1) // 2
    return seq_size - 1 - half, half


def solve(n, k):
    seqs = OrderedDict()
    seqs[n] = 1
    while True:
        size, count = seqs.popitem(last=False)
        if k > count:
            k -= count
            a, b = split(size)
            seqs[a] = seqs.get(a, 0) + count
            seqs[b] = seqs.get(b, 0) + count
        else:
            return split(size)


def main():
    next(sys.stdin)
    for t, line in enumerate(sys.stdin, 1):
        n, k = (int(x) for x in line.split())
        max_dist, min_dist = solve(n, k)
        print "Case #{}: {} {}".format(t, max_dist, min_dist)

main()

