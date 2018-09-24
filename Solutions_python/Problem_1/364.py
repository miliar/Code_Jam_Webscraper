#!/usr/bin/env python
# encoding: utf-8
"""
universe.py

Created by Devin Naquin on 2008-07-17.
Copyright (c) 2008. All rights reserved.
"""

import sys

def main():
    num_tests = int(sys.stdin.readline().strip())
    assert(1 <= num_tests and num_tests <= 20)
    
    for i in range(num_tests):
        num_se = int(sys.stdin.readline().strip())
        engines = []
        for j in range(num_se):
            engines.append(sys.stdin.readline().strip())
        num_qy = int(sys.stdin.readline().strip())
        queries = []
        for j in range(num_qy):
            queries.append(sys.stdin.readline().strip())
        
        assert(2 <= num_se and num_se <= 100)
        assert(0 <= num_qy and num_qy <= 1000)
        
        count = -1 if queries else 0
        while queries:
            longest, engine = find_longest(engines, queries)
            queries = queries[longest:]
            count += 1
        
        print 'Case #%s: %s' % (i+1, count)

def find_longest(engines, queries):
    longest_length = 0
    engine_to_use = None
    for eng in engines:
        try:
            length = queries.index(eng)
        except ValueError:
            # Not in queries
            length = len(queries) + 1
        if length > longest_length:
            longest_length = length
            engine_to_use = eng
    return longest_length, engine_to_use

if __name__ == '__main__':
    main()
