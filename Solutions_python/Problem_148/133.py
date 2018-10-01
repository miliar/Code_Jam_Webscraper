import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob
from bisect import bisect_left

taskname = 'A'
input = None

def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def solvecase():
    num_discs, capacity = readintlist()
    file_sizes = readintlist()
    assert len(file_sizes) == num_discs
    file_sizes.sort()
    disc_count = 0
    left = 0
    right = len(file_sizes)
    while right - left:
        right -= 1
        if left < right and file_sizes[left] + file_sizes[right] <= capacity:
            left += 1
        disc_count += 1
    return disc_count

def solve(input_name, output_name):
    global input
    tstart = time.clock()
    input = open(input_name, 'r')
    output = open(output_name, 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (input_name, time.clock() - tstart)

def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
