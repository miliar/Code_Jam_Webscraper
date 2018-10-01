#!/usr/bin/env python

# Audience of known shyness_levels si
#   si = 0 will stand up and clap immediately
#   si = 2 will stand up and clap if 2 others are
#
# minimum number of friends to invite (wich chosen shyness levels) to get everyone to stand and cheer
#
# Input:
#   # of test cases
#   s_max (maximum shyness level of the shyest person) s_max + 1 single digits of k shyness (where k is the zero based index of the string of numbers)
#
#     4
#     4 11111
#     1 09
#     5 110011
#     0 1
#
# Output:
#   Case #x: y (x is the test case, starting at 1, and y is the minimum number of friends)
#
#    Case #1: 0
#    Case #2: 1
#    Case #3: 2
#    Case #4: 0
#
# Min number of friends = max shyness level - number of people present below max shyness level

import sys


if __name__ == "__main__":

    file = sys.argv[1]

    with open(file) as fh:
        fh.readline() # Strip first line, don't need it
        case_num = 0

        for line in fh:
            s_max, audience = line.split()

            case_num += 1

            audience = list(audience)
            s_max = int(s_max)

            needed_friends = 0
            standing = 0
            shyness = 0
            for members in audience: # step through each shyness level
                if shyness == s_max:
                    break
                standing += int(members)
                if standing <= shyness:
                    needed_friends += 1
                    standing += 1
                shyness += 1

            print "Case #%d: %d" % (case_num, needed_friends)
