#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser('CodeJam Problem')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-i', '--infile', metavar='INFILE', 
                    help='input file to process, stdin if omitted')
args = parser.parse_args()

if args.infile:
    f_in = open(args.infile)
else:
    f_in = sys.stdin

def solve(query):
    return None # Replace...

lines = [line.strip() for line in f_in if line.strip()]
trial_tot = int(lines[0])
# print("{} total trials\n".format(trial_tot), file=sys.stderr)
lindex = 1
trial_num = 1
while lindex < len(lines):
    # print(60 * '=', file=sys.stderr)
    # print(lines[lindex])
    D, N = map(int, lines[lindex].split())
    lindex +=1
    times = []
    for h in range(N):
        K, S = map(int, lines[lindex].split())
        times.append((D-K)/S)
        lindex +=1
    # print(times)
    print("Case #{}: {:f}".format(trial_num, D/max(times)))
    trial_num +=1

#
#        print("Case #{}: ".format(trial_num))
#
#
#
#    for line_num, line in enumerate(f_in):
#        if line_num == 0:
#            trials = int(line.strip())
#            continue
#        answer = solve(line.strip())
#        print("Case #{:d}: {}".format(line_num, answer))
    
f_in.close()
