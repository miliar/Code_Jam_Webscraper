#from __future__ import division

from Tools import gcj
#from __future__ import division
#from functools32.functools32 import lru_cache
import sys
import itertools
import os
import re
import string
import math
import sys
import heapq
from collections import namedtuple, defaultdict, deque
from Tools.gcj import printd
from copy import deepcopy
#from simpleai.search import SearchProblem, astar
import random
import operator
#from Tools import primes
#from itertools import product

#return last index which is tidy. if last index == length(s), it is tidy
def last_index_tidy(s):
    last_index = 0
    prev = None
    for (i, v) in enumerate(s):
        v = int(v)
        if prev is not None and v < prev:
            return i - 1
        prev = v
    return len(s)

def replace_from_last_index(s, last):
    if s[last] == '1':
        #encojer
        return '9' * (len(s) - 1)
    else:
        new_str = ""
        if (len(s[0:last]) > 0):
            new_str += str(s[0:last])

        new_str += str(int(s[last]) - 1)
        new_str += '9' * (len(s) - last - 1)
        return new_str


def solver(n):
    i = n
    while i > 0:
        s = str(i)
        last = last_index_tidy(s)
        if last == len(s):
            return i
        else:
            s = replace_from_last_index(s, last)
            i = int(s)

    return

def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    n = in_file.getInt()

    return {
        'n': n,
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
