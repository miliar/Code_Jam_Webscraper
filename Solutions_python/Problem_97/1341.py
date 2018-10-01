import os
import sys
from itertools import permutations

from utils import stripped_lines, ints

def recycles(i, mn=float('-inf'), mx=float('inf')):
    def within_bounds(i):
        return mn <= i <= mx

    if within_bounds(i):
        yield i

    num = str(i)
    for i in range(len(num) - 1):
        num = num[-1] + num[:-1]
        if not num[0] == '0':
            r = int(num)
            if within_bounds(r):
                yield r

def ordered_pairs(nums):
    return ((a, b) for a, b in permutations(nums, 2) if a < b)

def solve(a, b):
    results = set()
    for n in xrange(a, b):
        rs = recycles(n, a, b)
        for pair in ordered_pairs(rs):
            results.add(pair)

    return len(results)

def main():
    fin_name = sys.argv[1]
    with open(fin_name) as fin:
        lines = stripped_lines(fin)

        numcases = int(lines.next())

        for caseno in range(1, numcases+1):
            a, b = ints(lines.next())
            result = solve(a, b)
            
            outstr = 'Case #%d: %s' % (caseno, result)
            print outstr

if __name__ == '__main__':
    main()