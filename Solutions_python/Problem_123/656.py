#
# By Allan Douglas R. de Oliveira
# This program is under public license
# 
########################
# makes python 2.x behave like python 3k
from __future__ import print_function, unicode_literals, division
# common imports
import sys
import operator
import math
from io import StringIO
from itertools import chain, combinations, product, permutations, islice
from collections import namedtuple
from functools import reduce
if sys.version_info[0] >= 3:
    #import numpy as np
    pass
else:
    # for pypy until it doesn't support py3k
    from itertools import izip as zip, ifilter as filter, imap as map
    range = xrange
    # numpypy may not work well on windows, yet
    #import numpypy as np
    
# integer square root
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# Parallel map with switch to serial map
def pmap(f, iterable, parallel=True):
    if parallel:
        from multiprocessing import Pool
        p = Pool(7)
        return p.imap(f, iterable, chunksize=1)
    else:
        return map(f, iterable)

def dot_product(v1, v2, sum=sum, map=map, mul=operator.mul):
    return sum(map(mul, v1, v2))

# some linalg utility definitions
Line = namedtuple('Line', 'A, B, C') # Line is Ax + By = C
Point = namedtuple('Point', 'x, y')

def iszero(n):
    return abs(n) < 1e-12

def point_to_line(p1, m):
    A, B, C = (m, -1, m*p1.x - p1.y)
    return Line(A, B, C)

def points_to_line(p1, p2):
    L = p2.y - p1.y
    K = p2.x - p1.x
    A, B, C = (L, -K, L * p1.x - K * p1.y)
    return Line(A, B, C)

def line_intersection2D(line1, line2):
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    det = A1*B2 - A2*B1
    if iszero(det): # parallel
        return None
    else:
        x = (B2*C1 - B1*C2) / det
        y = (A1*C2 - A2*C1) / det
        return Point(x, y)   

def calc_coord_y(line, x):
    y = (line.C - line.A * x) / line.B
    return y
# end of standard stuff
########################


sample_input = StringIO('''4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1''')


def check(motes_ordered, A):
    for i, mote in enumerate(motes_ordered):
        if A > mote:
            A += mote
        else:
            return (i, A)
    return None

def try_delete(i, motes_ordered, A, changes):
    #print ('try delete', A, changes, motes_ordered)
    motes_deleted = motes_ordered[i:-1]
    return process(motes_deleted, A, changes + 1)

def try_add(i, motes_ordered, A, changes):
    #print ('try add', A, changes, motes_ordered)
    #minimum_new_mote_size = motes_ordered[i] - A + 1
    #assert minimum_new_mote_size > 0
    if A <= 1:
        return None
    maximum_new_mote_size = A - 1
    results = []
    for new_mote_size in range(maximum_new_mote_size, maximum_new_mote_size+1):
        motes_added_new = [new_mote_size] + motes_ordered[i:]
        process_result = process(motes_added_new, A, changes + 1)
        if process_result is not None:
            results.append(process_result)
    return None if len(results) == 0 else min(results)

def process(motes_ordered, A, changes):
    #print (A, changes, motes_ordered)
    if len(motes_ordered) == 0:
        #print ('empty list, returning')
        return changes
    result = check(motes_ordered, A)
    if result is None:
        return changes
    else:
        i, a = result
        result_delete = try_delete(i, motes_ordered, a, changes)
        result_add = try_add(i, motes_ordered, a, changes)
        assert result_delete is not None or result_add is not None
        if result_delete is None:
            return result_add
        elif result_add is None:
            return result_delete
        else:
            return min(result_add, result_delete)

def process_test_case(inputs):
    A, N, motes = inputs
    motes_ordered = sorted(motes)
    
    changes = 0
    process_result = process(motes_ordered, A, changes)
    assert process_result is not None
    return process_result
            
    
    
def read_test_case(f):
    A, N = [int(x) for x in f.readline().split()]
    motes = [int(x) for x in f.readline().split()]
    return (A, N, motes)


def print_result(i, result):
    if result is None:
        print('Case #%d: %s' % (i+1, 'Error'))
    else:
        print('Case #%d: %d' % (i+1, result))

##########################
# basic test case reading and processing skeleton
def read_test_cases(f):
    T = int(f.readline())
    return [read_test_case(f) for t in range(T)]

def main(stream, parallel):
    for i, result in enumerate(pmap(process_test_case, read_test_cases(stream), parallel=parallel)):
        print_result(i, result)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(open(sys.argv[1]), True)
    else:
        main(sample_input, False)
##########################