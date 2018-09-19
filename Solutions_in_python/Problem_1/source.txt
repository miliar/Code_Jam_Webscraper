#! /usr/bin/env python

from __future__ import with_statement

import sys

def read_case(handle):
    num_engines = int(handle.readline().strip())
    engines = []
    for idx in range(num_engines):
        engines.append(handle.readline().strip())
    num_queries = int(handle.readline().strip())
    available = []
    for idx in range(num_queries):
        curr = set(engines)
        curr.remove(handle.readline().strip())
        available.append(curr)
    return (engines, available)

def solve_case(engines, available):
    row = {}
    for eng in engines:
        row[eng] = 0
    for idx in range(1,len(available)):
        curr = dict(row.iteritems())
        for eng in engines:
            if eng not in available[idx] and eng in curr:
                del curr[eng]
            elif eng in available[idx-1]:
                curr[eng] = row[eng]
            else:
                curr[eng] = min(row.itervalues()) + 1
        row = curr
    return min(row.itervalues())

def main():
    if len(sys.argv) != 2:
        print "usage: %s input_file" % sys.argv[0]
        exit(-1)
    num_cases = []
    cases = []
    with open(sys.argv[1]) as handle:
        num_cases = int(handle.readline().strip())
        for idx in range(num_cases):
            cases.append(read_case(handle))
    for idx, case in enumerate(cases):
        ret = solve_case(case[0], case[1])
        print "Case #%d: %d" % (idx+1, ret)

if __name__ == '__main__':
    main()