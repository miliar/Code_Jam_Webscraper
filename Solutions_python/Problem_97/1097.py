#!/usr/bin/python -tt

import sys

def pairs(a,b):
    n = len(str(a))
    assert n == len(str(b))
    total = 0
    for i in range(a,b):
            pairs = []
            for j in range(n):
                    k = int(str(i)[j:]+str(i)[:j])
                    if k not in pairs:
                        pairs.append(k)
                        if k > i and k <= b:
                            total += 1
    return total

def parse_case(input_file):
    with open(input_file) as f:
        n_test_cases = int(f.readline())
        cases = []
        for case in xrange(n_test_cases):
            cases.append(map(int, f.readline().split()))
    return cases

def jam(case):
    return pairs(case[0],case[1])

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    cases = parse_case(sys.argv[1])
    i = 0
    for case in cases:
        i += 1
        print 'Case #%d: %d' % (i, jam(case))

if __name__ == '__main__':
    sys.exit(main())


