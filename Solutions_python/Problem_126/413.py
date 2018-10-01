#!/usr/bin/python

import sys, math

vowels = 'aeiou'

def solve(case):
    (name, n) = (case[0], int(case[1]))
    cons = set([i for i in range(len(name) - n + 1) if all(letter not in vowels for letter in name[i : i + n])])

    n_value = 0

    for i in range(len(name) - n + 1):
        for l in range(1, len(name) - i - n + 2):
            # print 'Range: %s' % name[i:i+l]
            if any(index in cons for index in range(i, i + l)):
                n_value += 1

    return n_value

input = [line.strip().split() for line in sys.stdin]
for index in range(1, int(input[0][0]) + 1):
    print 'Case #%d: %d' % (index, solve(input[index]))
