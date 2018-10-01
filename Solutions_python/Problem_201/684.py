#!/usr/bin/env python3

import sys

from collections import Counter

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

def find_used(k):
    pow = 0
    required = 0
    last_required = required
    while required < k:
        last_required = required
        required += 2**pow
        pow += 1
    return last_required, 2**(pow-1)


def case(n, k):
    used_up_cells, gaps = find_used(k)
    to_use_cells = k - used_up_cells
    empty_cells = n - used_up_cells

    min_gap = empty_cells // gaps
    additional_empty_cells = empty_cells - min_gap * gaps

    gap_size = min_gap + (1 if additional_empty_cells >= to_use_cells else 0)

    min_d = (gap_size - 1) // 2
    max_d = gap_size // 2

    return '{} {}'.format(max_d, min_d)


####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    #in_file_name = 'C-small-2-attempt0.in'
    in_file_name = 'C-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        n, k = read_ints()
        solution = case(n, k)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


####################################################################
#                             Tests                                #
####################################################################


def test_find_used():
    assert find_used(1) == (0, 1)
    assert find_used(2) == (1, 2)
    assert find_used(3) == (1, 2)
    assert find_used(4) == (3, 4)
    assert find_used(5) == (3, 4)
    assert find_used(6) == (3, 4)
    assert find_used(7) == (3, 4)
    assert find_used(8) == (7, 8)


if __name__ == '__main__':
    main()
    #tests()
