from itertools import product, combinations

import collections

from collections import defaultdict, Counter

import heapq
import sys
import math
from multiprocessing.pool import Pool

from sortedcontainers import SortedDict
from tqdm import tqdm

################################################################################

CONCURRENCY = 0

eps = 1e-6
MAX = 999999999999999999

def solve(case_inputs):
    N, K, pans = case_inputs

    pans = sorted(pans, reverse=True)

    best_sc = 0
    for i in range(N-K+1):
        # print(i, N, K)
        r, h = pans[i]
        sc = score(r, h)
        scores = []
        # print(i+1)
        for j in range(i+1, N):
            r, h = pans[j]
            scores.append(part_score(r, h))
        # print(scores)
        scores.sort(reverse=True)
        for j in range(K-1):
            sc += scores[j]

        best_sc = max(best_sc, sc)

    return best_sc

def score(r, h):
    pi = math.pi
    return pi * (r**2) + 2*pi*r*h

def part_score(r,h):
    pi = math.pi
    return 2 * pi * r * h

def full_score(r, h, max_r):
    pi = math.pi
    sc = part_score(r, h)
    if r > max_r:
        sc -= pi * (max_r**2)
        sc += pi * (r**2)
    return sc

################################################################################

def read_case(f):
    N, K = read_ints(f)
    pans = [read_ints(f) for _ in range(N)]
    return N, K, pans

def write_case(f, i, res):
    f.write('Case #%s: '%i)
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

def out_file(in_file):
    return in_file[:in_file.rfind('.')] + '.out'

def main():
    if len(sys.argv) != 2:
        print('usage: python <file_name> <input_file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f, open(out_file(sys.argv[1]), 'w') as w:
        count = read_int(f)
        if CONCURRENCY > 0:
            solve_concurrent(CONCURRENCY, count, f, w)
        else:
            solve_single_process(count, f, w)

def solve_concurrent(CONCURRENCY, count, f, w):
    problems = [read_case(f) for _ in range(count)]
    with Pool(CONCURRENCY) as p:
        solutions = p.map(solve, problems)
    assert len(solutions) == count
    for i in tqdm(range(count), desc='[** CONCURRENCY={} **] Writing solutions to output file'.format(CONCURRENCY)):
        write_case(w, i + 1, solutions[i])

def solve_single_process(count, f, w):
    for i in tqdm(range(1, count + 1), desc='Solving problems and writing solutions to output file'):
        print(i)
        case_inputs = read_case(f)
        write_case(w, i, solve(case_inputs))


if __name__ == "__main__":
    main()


