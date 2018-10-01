#!/usr/bin/env python

from __future__ import print_function, division
__metaclass__ = type

import sys, re, string, struct, math
import itertools, collections
import numpy as np

from itertools import *

class Namespace:
    pass


def readlines_g(f, strip=True, split=False, limit=None, convert=None):
    if convert is None:
        convert = lambda x: x
    i = 0
    for line in f:
        if limit is not None and i >= limit:
            break
        if strip:
            line = line.strip()
        if split:
            line = [convert(x) for x in line.split()]
        else:
            line = convert(line)
        yield line
        i += 1

def readlines(*args, **kwargs):
    return list(readlines_g(*args, **kwargs))

def readline(*args, **kwargs):
    for line in readlines_g(*args, **kwargs):
        return line


# http://code.activestate.com/recipes/65212/
def baseN(num, base, numerals=list(range(10))):
    if num == 0:
        return "0"
    if num < 0:
        return '-' + baseN((-1) * num, base, numerals)
    if not 2 <= base <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))
    left_digits = num // base
    if left_digits == 0:
        return [numerals[num % base]]
    else:
        return baseN(left_digits, base, numerals) + [numerals[num % base]]


happiness = dict((i,[False,True] + [None]*1000) for i in range(2,11))
def is_happy(n, base):
    if len(happiness[base]) < n+1:
        happiness[base] += [None] * (n+1 - len(happiness[base]))
    h = happiness[base]
    seen = set([n])
    old_len = 0
    while len(seen) > old_len:
        old_len = len(seen)
        n = sum(x*x for x in baseN(n,base))
        v = h[n]
        if v is True:
            for x in seen:
                h[x] = True
            return True
        elif v is False:
            for x in seen:
                h[x] = False
            return False
        seen.add(n)
    for x in seen:
        h[x] = False
    return False

def first_happy(bases):
    for i in count(2):
        if all(is_happy(i, b) for b in bases):
            return i

def run(f):
    T = int(readline(f))
    for case_no in range(1,T+1):
        bases = readline(f, split=True, convert=int)
        answer = first_happy(bases)
        print('Case #{0}: {1}'.format(case_no, answer))

if __name__ == "__main__":
    try:
        filename, = sys.argv[1:]
    except ValueError:
        print('USAGE: %s filename'%sys.argv[0], file=sys.stderr)
        sys.exit(1)
    with open(filename) as f:
        run(f)
