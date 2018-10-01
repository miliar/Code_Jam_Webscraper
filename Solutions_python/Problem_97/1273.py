#!/usr/bin/env python
import sys


def is_recycled_pair(a, b):
    a = str(a)
    b = str(b)
    return b in (a[i:]+a[:i] for i in range(len(b)))

class Case(object):
    def __init__(self, a, b):
        self.a, self.b = a, b

    @classmethod
    def parse(cls, f):
        a, b = (int(x) for x in f.readline().strip().split(' '))
        return Case(a, b)

    def solve(self):
        pairs = 0
        for i in range(self.a, self.b):
            for j in range(i+1, self.b+1):
                if is_recycled_pair(i, j):
                    pairs += 1
        return pairs


def parse(f):
    case_count = int(f.readline().strip())
    cases = []

    for i in range(case_count):
        cases.append(Case.parse(f))

    results = [c.solve() for c in cases]

    for i, d in enumerate(results, start=1):
        print 'Case #%d: %d' % (i, d)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        parse(f)
