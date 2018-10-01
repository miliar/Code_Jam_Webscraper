#!/usr/bin/python

from sys import stdin,stdout

# Read in input
num_problems = int(stdin.readline())

for problem_number in range(1, num_problems + 1):
    N, Pd, Pg = [int(x) for x in stdin.readline().split(' ')]

    print "Case #" + str(problem_number) + ":",
    for x in range(1, min(101, N+1)):
        if (Pd * x) % 100.0 == 0.0:
            if not (Pg == 100 and Pd != 100):
                if not (Pg == 0 and Pd != 0):
                    print "Possible"
                    break
    else:
        print "Broken"

    # Output template

