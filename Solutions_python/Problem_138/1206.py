#!/usr/bin/python

import sys

def war(b1, b2):
    #b1 = set(b1)
    b2 = set(b2)

    score = 0

    for w1 in b1:
        candidates = [w for w in b2 if w > w1]
        if len(candidates) == 0:
            b2.remove(min(b2))
            score += 1
        else:
            b2.remove(min(candidates))
    return score

def dwar(b1, b2):
    b1 = set(b1)
    b2 = set(b2)

    score = 0
    for w1 in sorted(b1):
        s_candidates = [w for w in b2 if w < w1]
        if len(s_candidates) == 0:
            b2.remove(max(b2))
        else:
            b2.remove(max(s_candidates))
            score += 1
    return score

def solve(b1, b2):
    return dwar(b1, b2), war(b1, b2)

def read_case(f):
    blocks = int(f.readline())
    b1 = [float(v) for v in f.readline().split()]
    b2 = [float(v) for v in f.readline().split()]
    assert(len(b1) == len(b2) == blocks)
    return b1, b2


def main(filename):
    with open(filename) as f:
        for case_num in range(int(f.readline())):
            b1, b2 = read_case(f)
            w, dw = solve(b1, b2)
            print 'Case #{}: {} {}'.format(case_num + 1, w, dw)

if __name__ == "__main__":
    main(sys.argv[1])
