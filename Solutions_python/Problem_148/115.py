from __future__ import division
from functools32.functools32 import lru_cache
import sys
import itertools
import os
import re
import string
import math
import sys
import heapq
from collections import namedtuple, defaultdict, deque
from Tools import gcj
from Tools.gcj import printd
from bitstring import BitArray, BitStream
from copy import deepcopy
from simpleai.search import SearchProblem, astar
import random
import operator
#from Tools import primes

def is_solvable(n_buckets, capacity, sizes):
    #printd("is_solvable", n_buckets, capacity, sizes)
    if capacity * n_buckets < sum(sizes):
        #printd("NOT ENOUGH")
        return False

    if n_buckets >= len(sizes):
        #printd("TOO MUCH")
        return True

    free = dict()
    for i in xrange(n_buckets):
        rem = capacity - sizes[i]
        if rem > 0:
            free[i] = rem

    disks = sorted(sizes[n_buckets:])
    #printd("remaining", free)
    #printd("disks", disks)

    for d in disks:
        found = False
        for k in free.iterkeys():
            if free[k] >= d:
                found = True
                free[k] = 0
                del free[k]
                break
        if not found:
            return False

    #printd("YES SOLVABLE")
    return True

    #printd("total buckets", n_buckets)
    #printd("remaining disks", disks)
    #printd("free ", free)
    #for i in xrange(len(sizes) - 1, n_buckets - 1, - 1):

def search_size(capacity, sizes):
    hi = len(sizes)
    lo = int(math.ceil(len(sizes) / 2))
    printd("HI", hi, "LO", lo)

    while hi != lo:
        mid = (hi + lo) // 2
        solved = is_solvable(mid, capacity, sizes)

        if solved:
            #printd("Checking ", hi, lo, "    MID=", mid, "   solved? YES", groups)
            hi = mid
        else:
            printd("Checking ", hi, lo, "    MID=", mid, "   solved? NO")
            if lo >= mid:
                lo += 1
            else:
                lo = mid
    return lo


def solver(num_files, x, sizes):
    sizes = sorted(sizes, reverse=True)
    printd(sizes)

    return search_size(x, sizes)

    pass


def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    n, x = in_file.getInts()
    sizes = in_file.getInts()

    return {
        'num_files': n, 'x': x, 'sizes': sizes,
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
