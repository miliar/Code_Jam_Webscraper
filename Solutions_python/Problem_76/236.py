#!/usr/bin/env python

from sys import argv

def partition(candies):
    if reduce(lambda x, y: x^y, candies) != 0:
        return "NO"
    return sum(candies) - min(candies)

if __name__ == "__main__":
    with open(argv[1], "r") as f:
        cases = int(f.readline())
        for i in range(cases):
            # Throw line away
            f.readline()
            candies = map(int, f.readline().split())
            print "Case #%d: %s" % (i + 1, partition(candies))
