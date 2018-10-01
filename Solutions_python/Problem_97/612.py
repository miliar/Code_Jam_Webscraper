#!/usr/bin/env python
#
# Google Code Jam 2012
# Nathan Williams <nlwsother@gmail.com>
# Qualification Round, Problem C, Recycled Numbers
#

import sys

DEBUG = False
ERROR = True
OUTPUT = True
RUN_TEST_CASE = False

def log(do_log, s):
    if do_log:
        print str(s)


def count_pairs(A, B):
    log(DEBUG, "Finding pairs between (%d,%d)" % (A,B))
    distinct_set = set()
    curA = A
    while curA <= B:
        n = curA
        nStr = str(n)
        i = 1
        while i < len(nStr):
            rec = nStr[i:] + nStr[:i]
            if rec[0] != '0':
                m = int(rec)
                if n < m and m <= B:
                    tup = (n,m)
                    #log(DEBUG, "%s:%s" % (nStr, tup))
                    distinct_set.add(tup)
            i += 1
        curA += 1
    return len(distinct_set)


if RUN_TEST_CASE:
    tests = { (0,0) : 0, (1,9) : 0, (10,40) : 3, (100,500) : 156, (1111,2222) : 287 }
    for k,v in tests.iteritems():
        counted = count_pairs(k[0], k[1])
        if counted != v:
            log(ERROR, "TEST FAILED %s: expected=%d got=%d" % (k, v, counted))



if len(sys.argv) == 1:
    sys.exit(0)
elif len(sys.argv) > 2:
    log(DEBUG, "Too many command line arguments")


log(DEBUG, "Processing %s\n" % sys.argv[1])

read_count = False
read_lines = 0
input_file = open(sys.argv[1])

for cur_line in input_file:
    if read_count is False:
        read_count = int(cur_line)
    elif read_lines == read_count:
        break
    else:
        read_lines += 1
        # Spec: no spaces at begin or end of line
        split_text = cur_line.strip().split(' ')
        if len(split_text) != 2:
            log(ERROR, "Malformed split_text: %s" % str(split_text))
        else:
            counted = count_pairs(int(split_text[0]), int(split_text[1]))
            log(OUTPUT, 'Case #%d: %d' % (read_lines, counted))

input_file.close()
