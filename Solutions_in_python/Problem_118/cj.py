#!/usr/bin/env python3

import collections
import functools
import itertools
import math
import operator
import sys

def read_int():
    return int(input())

def read_ls():
    return [int(x) for x in input().split()]

def memoize(f):
    cache = {}
    @functools.wraps(f)
    def aux(*x):
        nonlocal cache
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return aux

@memoize
def is_fair(n):
    """
    check if an integer is a palindrome
    """
    assert(type(n) == int)
    s = str(n)
    i = 0

    while i < int(len(s) / 2):
        if s[i] != s[len(s) - (i+1)]:
            return False
        i += 1

    return True

def is_square(n):
    """
    check if the square root of an integer is an integer and the square is a
    palindrome
    """
    assert(type(n) == int)
    sq = math.sqrt(n)
    return sq == int(sq) and is_fair(int(sq))

@memoize
def is_fair_and_square(n):
    return is_square(n) and is_fair(n)

def run(low, high):
    return sum(map(is_fair_and_square, range(low, high+1)))

def main():
    for i in range(read_int()):
        # input data
        low, high = read_ls()

        # evaluate
        result = run(low, high)

        # output
        print("Case #%d: %d" % (i+1, result))

if __name__ == "__main__":
    sys.exit(main())
