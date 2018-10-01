#!/usr/bin/env python

"""Google Code Jam 2009, Qualification round."""

import sys

def read_bin_matrix(fh, num):
    V = []
    for i in range(num):
        row = fh.readline()
        V.append(row.rfind("1") + 1)
    return V

def satisfied(V):
    row = 0
    for v in V:
        if v > row + 1:
            return row
        row += 1
    return -1

def bubble_up(V, row):
    for i in range(row+1, len(V)):
        if V[i] <= row+1:
            v = V.pop(i)
            V.insert(row,v)
            return i - row

def calc_res(V):
    swaps = 0
    fix_row = satisfied(V)
    while fix_row != -1:
        swaps += bubble_up(V, fix_row)
        fix_row = satisfied(V)
    return swaps

def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            N = int(f.readline())
            V = read_bin_matrix(f, N)
            print "Case #" + str(case+1) + ": " + str(calc_res(V))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
