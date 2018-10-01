#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from functools import reduce

input_file = open(sys.argv[1])
if len(sys.argv) > 2:
    ouput_file = open(sys.argv[2], 'w')

def parse(line):
    candy = tuple(map(int, line.split()))

    return candy


def solve(line):
    candy = parse(line)

    if reduce(int.__xor__, candy) == 0:
        answer = sum(candy) - min(candy)
    else:
        answer = 'NO'

    return answer

cases = int(next(input_file))

for case in range(1, cases + 1):
    next(input_file)
    print('Case #{case}: {result}'.
          format(case=case, result=solve(next(input_file))),
          file=ouput_file if len(sys.argv) > 2 else sys.stdout, )
