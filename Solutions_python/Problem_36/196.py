#!/usr/bin/env python

from __future__ import print_function, division
__metaclass__ = type

import sys, re, string
import numpy as np

class Namespace:
    pass

def count_jam(line, s = "welcome to code jam"):
    count = 0
    pos = 0
    if len(s) == 1:
        return line.count(s)
    x, rest = s[0], s[1:]
    for pos in range(len(line)-len(s)+1):
        if line[pos] == x:
            count += count_jam(line[pos+1:], rest)
    return count

def run(filename):
    with open(filename) as f:
        for line in f:
            T = int(line.strip())
            break
        for i,line in enumerate(f):
            print('Case #{0}: {1:04}'.format(i+1, count_jam(line)))

if __name__ == "__main__":
    try:
        filename, = sys.argv[1:]
    except ValueError:
        print('USAGE: %s filename'%sys.argv[0], file=sys.stderr)
        sys.exit(1)
    run(filename)
