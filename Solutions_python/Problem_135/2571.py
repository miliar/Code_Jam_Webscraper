#!/usr/bin/env python
import sys

# Initalizing file and number of cases
f = open(sys.argv[1], 'r')
num_cases = int(f.readline())

# For each case, make guess, mistake, or cheat!
for x in range(1, num_cases+1):

    # Initial row placement
    row_init = int(f.readline())
    pos_init = []
    for y in range(0, 4):
        pos_init.append(f.readline().split())

    # Final row placement
    row_final = int(f.readline())
    pos_final = []
    for y in range(0, 4):
        pos_final.append(f.readline().split())

    # Magic!
    num_overlap = 0
    magic_numbers = [val for val in pos_init[row_init-1] if val in pos_final[row_final-1]]
    num_overlap = len(magic_numbers)
    
    # Guess, mistake or cheat?
    if (num_overlap == 0): output = "Volunteer cheated!"
    elif (num_overlap > 1): output = "Bad magician!"
    else: output = magic_numbers.pop(0)

    # Output guess
    print "Case #" + str(x) + ": " + str(output)
