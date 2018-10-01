#!/usr/bin/env python3

import sys
from collections import Counter
from math import pi


####################################################################
#                           Helpers                                #
####################################################################


def read_int():
    return int(input())


def read_ints():
    return [int(s) for s in input().split()]


####################################################################
#                           Solution                               #
####################################################################


def solve_others(sorted_by_border, i, bottom_p, k):
    r, _ = bottom_p
    cnt = 0
    sum = 0.0
    for j, p, border in sorted_by_border:
        if j != i and p[0] <= r:
            cnt += 1
            sum += border
            assert cnt <= k
            if cnt == k:
                break

    if cnt != k:
        sum = 0.0

    return sum


def test_case(pancakes, k):
    def border(p):
        r, h = p
        per = pi * 2 * r
        return per * h
    pp = [(i, p, border(p)) for i, p in enumerate(pancakes)]
    sorted_by_border = sorted(pp, key=lambda p: -p[2])

    best = 0.0
    for i, bottom_p in enumerate(pancakes):
        if k > 1:
            borders = solve_others(sorted_by_border, i, bottom_p, k-1)
        else:
            borders = 0.0
        rr, hh = bottom_p

        v = borders + pi * rr*rr + border(bottom_p)
        best = max(best, v)
    return best


####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    #in_file_name = 'A-small-attempt0.in'
    in_file_name = 'A-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        n, k = read_ints()
        pp = []
        for _ in range(n):
            pp.append(read_ints())
        solution = test_case(pp, k)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
