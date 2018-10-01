#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser('CodeJam Problem: tidy numbers')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-i', '--infile', metavar='INFILE', 
                    help='input file to process, stdin if omitted')
args = parser.parse_args()

if args.infile:
    f_in = open(args.infile)
else:
    f_in = sys.stdin

def num_sorted(numstr):
    """Determine whether the digits in the (decimal) string representation
    of a number are in sorted order."""
    return sorted(numstr) == list(numstr)

#  def lower(n, place, length):
#      return 10**(length-place) * int(n/(10**(length-place))) - 1

def lower(n, place, length):
    numstr = str(n)
    bottom = numstr[:place +1]
    top = (length - place) * '0'
    return (int(bottom + top) - 1)
       

def next_lowest_tidy(x):
    diglist = [int(digit) for digit in str(x)]
    while num_sorted(diglist) is False:
        for place, val in enumerate(diglist):
            if place >= len(diglist) -1:
                break
            if val > diglist[place+1]:
                x = lower(x, place, len(diglist)-1)
                diglist = [int(digit) for digit in str(x)]
    return x
        
    

for line_num, line in enumerate(f_in):
    if line_num == 0:
        trials = int(line.strip())
        continue
    answer = next_lowest_tidy(int(line.strip()))
    print("Case #{:d}: {}".format(line_num, answer))
    
f_in.close()




