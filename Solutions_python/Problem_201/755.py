#!/usr/bin/env python3

import sys
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser('CodeJam Problem')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-i', '--infile', metavar='INFILE', 
                    help='input file to process, stdin if omitted')
args = parser.parse_args()

if args.infile:
    f_in = open(args.infile)
else:
    f_in = sys.stdin


def split_gap(gap_size):
    half = gap_size//2
    if gap_size % 2 == 1:
        return 2 * (half,)
    else:
        return (half-1, half)

def fill_stalls(stalls, people):
    gaps = defaultdict(int)
    gaps[stalls] = 1
    gap_size = max(gaps)
    # print("Preloop: gap_size: {}  people: {}  gaps:{}".format(gap_size, people, gaps))
    while people > gaps[gap_size]:
        # print("gap_size: {}  people: {}  gaps:{}".format(gap_size, people, gaps))
        gap_size = max(gaps)
        gap_count = gaps[gap_size]
        # moves = min(gap_count, people)
        # Get the two new sizes from splitting the gap
        # print("Here's my gap size: {}".format(gap_size))
        new_size1, new_size2 = split_gap(gap_size)
        gaps[new_size1] += gap_count
        gaps[new_size2] += gap_count
        del gaps[gap_size]
        gap_size = max(gaps) # New gap size to act on
        people -= gap_count
    # I'm done, so split the last gap_size to get the two answers
    return split_gap(gap_size)

for line_num, line in enumerate(f_in):
    if line_num == 0:
        trials = int(line.strip())
        continue
    stalls, people = map(int, line.strip().split())
    mingap, maxgap = fill_stalls(stalls, people)
    print("Case #{:d}: {} {}".format(line_num, maxgap, mingap))
    
f_in.close()
