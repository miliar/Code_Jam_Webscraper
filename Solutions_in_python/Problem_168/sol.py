
import math
import itertools
import numpy as NP

################################################################################

def read_case(f):
    R, C = read_ints(f)
    M = read_arr(f, R, read_letters)
    return R, C, M

def arrows(R, C, M, x, y, d):
    dx, dy = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }[d]
    while True:
        x += dx
        y += dy
        if x < 0 or x >= R or y < 0 or y >= C:
            return False
        if M[x][y] != '.':
            return True

def solve_small(case):
    R, C, M = case
    res = 0
    for x in range(R):
        for y in range(C):
            m = M[x][y]
            if m == '.':
                continue
            if arrows(R, C, M, x, y, m):
                continue
            for d in '^>v<':
                if d == m:
                    continue
                if arrows(R, C, M, x, y, d):
                    res += 1
                    break
            else:
                return 'IMPOSSIBLE'
    return res

def solve_large(case):
    return solve_small(case)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)

DEBUG = 'i'

from run import *
