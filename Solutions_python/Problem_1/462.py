#!/usr/bin/env python
'''
Google Code Jam 2008
Problem: Saving the Universe
Author: euphoria
'''

import sys

def compute_switches(engines, queries):
    switches = 0
    used = {}
    for query in queries:
        used[query] = True
        if len(used) == len(engines):
            switches = switches + 1
            used.clear()
            used[query] = True
    return switches
    
def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    f = open(argv[1])
    cases = int(f.readline())
    for case in xrange(1,cases+1):
        engines_num = int(f.readline())
        engines = [f.readline() for enum in xrange(engines_num)]
        queries_num = int(f.readline())
        queries = [f.readline() for qnum in xrange(queries_num)]
        
        switches = compute_switches(engines, queries)
        
        print 'Case #%s: %s' % (case,switches)
    f.close()
    
if __name__ == "__main__":
    sys.exit(main())