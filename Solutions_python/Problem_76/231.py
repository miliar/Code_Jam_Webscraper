#!/usr/bin/python
# -*- coding: utf-8 -*-

import re,os,sys

def pat_sum(ls):  return reduce( lambda a,b: a^b, ls)
def sean_sum(ls): return reduce( lambda a,b: a+b, ls)

def split_bag(bag):
    if pat_sum(bag) == 0:
        return sean_sum(bag) - min(bag)
    else:
        return None
    
def parse_file(fn):
    return parse_input(open(fn,'r').read())

def parse_input(s):
    cases = []
    lines = re.split(r'\r|\n|\r\n', s)
    T = int( lines.pop(0) )

    for t in range(T):
        n = int( lines.pop(0) )
        cs = [ int(c) for c in re.split(r'\s+', lines.pop(0)) ]

        if not n == len(cs): raise

        cases.append(cs)

    return cases

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cases = parse_file(sys.argv[1])
    else:
        cases = parse_input(sys.stdin.read())

    for t in range(len(cases)):
        m = split_bag(cases[t])
        
        if m is None:
            print "Case #%d: NO" % (t+1)
        else:
            print "Case #%d: %d" % (t+1, m)
