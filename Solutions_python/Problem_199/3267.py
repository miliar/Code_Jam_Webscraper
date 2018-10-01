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

def is_clean(s, start, end):
    c = True
    for v in s[start: end]:
        if v == '-':
            c = False
            break
    return c

def invert(v, start, k):
    for i in xrange(start, start + k):
        if v[i] == '+':
            v[i] = '-'
        else:
            v[i] = '+'

def solve_recursive(s, k, start, end):
    printd( "s", s, "k", start, end)
    if (end - start) == k:
        if is_clean(s, start, end):
            return 0
        elif s[start:end] == list('-' * k):
            return 1
        else:
            return None

    if s[start] == '-' or s[end - 1] == '-':
        options = []
        if s[start] == '-':
            s2 = deepcopy(s)
            invert(s2, start, k)
            cost = solve_recursive(s2, k, start + 1, end)
            if cost is not None:
                options.append(cost)
        if s[end - 1] == '-':
            printd("HERE", start, end)
            s2 = deepcopy(s)
            invert(s2, end - k, k)
            printd("INVERTED", s, s2)
            cost = solve_recursive(s2, k, start, end - 1)
            if cost is not None:
                options.append(cost)
        if len(options) > 0:
            return 1 + min(options)
        else:
            return None
    else:
        return solve_recursive(s, k, start + 1, end)

def solver(s,k):
    v = solve_recursive(s, k, 0, len(s))
    if v is None:
        return "IMPOSSIBLE"
    else:
        return v



def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    (s, k) = in_file.readline().split(" ")
    s = list(s)
    k = int(k)

    return {
        's': s,
        'k': k
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
