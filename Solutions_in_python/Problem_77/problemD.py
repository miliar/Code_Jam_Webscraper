#!/usr/bin/python
# -*- coding: utf-8 -*-

import re,os,sys

def parse_file(fn):
    return parse_input(open(fn,'r').read())

def parse_input(input):
    lines = re.split(r'\r|\n|\r\n', input)
    T = int( lines.pop(0) )

    cases = []
    for t in range(T):
        N = int( lines.pop(0) )
        array = [ int(x) for x in re.split(r'\s+', lines.pop(0) ) ]
        cases.append(array)
        if not len(array) == N: raise

    if not len(cases) == T: raise
    return cases


if __name__ == '__main__':
    if len(sys.argv) > 1:
        cases = parse_file(sys.argv[1])
    else:
        cases = parse_input(sys.stdin.read())

    for t in range(len(cases)):
        seq = cases[t]

        count = sum( [ int(i+1 != seq[i]) for i in range(len(seq)) ] )
        print "Case #%d: %.6f" % (t+1, count)
                           
