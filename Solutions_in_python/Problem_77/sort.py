# -*- coding: utf-8 -*-

import sys
import math

def solve_case(seq):
    seq = [int(i) for i in seq.split()]
    l = len(seq)
    flags = [True if seq[i] == i+1 else False for i in range(0, l)]
    prob = 0
    for i in range(0, l):
        if flags[i] == False:
            idx = seq.index(i+1)
            if idx+1 == seq[i]:
                flags[idx] = True
                flags[i] = True
                seq[i], seq[idx] = seq[idx], seq[i]
                prob += 2.0
    rest = l - sum(flags)
    if rest > 0:
        prob += math.factorial(rest) / math.factorial(rest - 1)
    return prob

def test():
    assert solve_case('2 1') == 2.0
    assert solve_case('1 3 2') == 2.0
    assert solve_case('2 1 4 3') == 4.0
    assert solve_case('1 2 3 4 5') == 0.0
    assert solve_case('1 4 3 2 5') == 2.0

if __name__ == '__main__':

    test()

    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        if f:
            out = open(sys.argv[1] + '.out', 'w')
            f.readline()
            idx = 1
            for line in f:
                seq = f.next()
                s = "Case #%s: %.6f\n" % (idx, solve_case(seq))
                out.write(s)
                idx += 1
        else:
            print 'Can not open file', sys.argv[1]
    else:
        print 'Ivalid arguments number'
