#!/usr/bin/env python

# Author: Uldis Bojars
#         captsolo.net

# PRINT_CASES = True
PRINT_CASES = False

import os


def read_paths(inp, out):
    paths = {}

    for item in inp:
        tmp = item
        while tmp != "/":
            paths[tmp] = True
            head, tail = os.path.split(tmp)
            tmp = head

    sum = 0
    for item in out:
        tmp = item
        i = 0
        while (tmp not in paths) and (tmp != "/"):
                if tmp not in paths:
                    paths[tmp] = True
                head, tail = os.path.split(tmp)
                tmp = head
                i += 1
        sum += i
    return sum
        
import sys
from cStringIO import StringIO


class TestCases(object):
    def __init__(self, test_arr):
        self.arr = list(test_arr)

    def cases(self):
        tmp = self.arr
        num_cases = int(tmp[0])

        pos = 1

        # for all test cases
        for i in range(0, num_cases):
            n, k, b, t = map(int, tmp[pos].split())
            pos += 1
            coord  = map(int, tmp[pos].split())
            pos += 1
            speed  = map(int, tmp[pos].split())
            pos += 1

            chicks = zip(coord, speed)
            #print chicks

            yield (chicks, n, k, b, t)

def chicken_run(data):
    chicks, n, k, b, t = data

    pos_t = []
    in_barn = 0
    for i in chicks:
        tmp = i[0] + t*i[1]
        pos_t.append(tmp)
    
        if tmp >= b:
            in_barn += 1

    from copy import copy
    pos_t_rev = copy(pos_t)
    pos_t_rev.reverse()

    in_barn = 0
    slow = 0
    jumps = 0

    for item in pos_t_rev:
        if item >= b:
            in_barn += 1
            jumps += slow
            if in_barn == k:
                break
        else:
            slow += 1

    #return (k, in_barn, jumps, in_barn >= k)
    if in_barn < k:
        jumps = "IMPOSSIBLE"
    return jumps

def run_test(test_file):
    tests = TestCases(test_file)
    for i, data in enumerate(tests.cases()):
        res = chicken_run(data)
        #res = read_paths(src, out)
        print "Case #%i: %s" % (i+1, res)


def main():
    import sys
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        f = open(fname)
    else:
        print "Usage: %s input_file" % (sys.argv[0],)
        print " - no parameters supplied. running example test case."
        print 
        f = mock_test()

    # f = open(fname)

    run_test(f)
    f.close()
 

if __name__ == "__main__":
    main()
