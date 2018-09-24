#!/usr/bin/env python

import sys

if __name__ == '__main__':
    testcase = int (sys.stdin.readline ())
    case = 1
    while (case <= testcase):
        changes = 0
        se_list = []
        num_se = int (sys.stdin.readline ())
        for i in xrange (num_se):
            se_name = sys.stdin.readline ().strip('\n')
            se_list.append (se_name)

        se_copy = se_list[:]
        num_queries = int (sys.stdin.readline ())
        idx = 0
        for i in xrange (num_queries):
            query = sys.stdin.readline().strip('\n')
            try:
                idx = se_copy.index (query)
            except ValueError:
                pass
            else:
                del se_copy[idx]
                #print se_copy
                #print len(se_copy)
                #print idx
                if len(se_copy) == 0:
                    changes += 1
                    se_copy = se_list[:]
                    se_copy.remove(query)

        print "Case #%d: %d" % (case, changes)
        case += 1
