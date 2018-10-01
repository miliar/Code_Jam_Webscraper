#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import math

def read(f):
    n = int(f.readline().rstrip())
    for i in xrange(n):
        C, F, X = map(float, f.readline().rstrip().split())
        yield C, F, X

def calc(n, c, f, x):
    # C * (1/2 + 1/(2+F) + 1/(2+2F) + 1/(2+3F) + ... + 1/(2+(n-1)F)) + X / (2+nF)
    t = 0
    for i in xrange(n):
        t += c / (2 + i * f)
    t += x / (2 + n * f)
    return t

def solve(c, f, x):
    n = max(0, int(math.ceil(x / c - 2 / f - 1)))
    return calc(n, c, f, x)

def main(f):
    for i, (c, f, x) in enumerate(read(f)):
        t = solve(c, f, x)
        print("Case #{0}: {1:.7f}".format(i + 1, t))

_input = """
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
""".strip()

_output = """
Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
""".strip()

def test_main(compare=False):
    import sys
    from difflib import unified_diff
    from StringIO import StringIO

    if compare:
        stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main(StringIO(_input))
            result = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = stdout

        print(result)

        for line in unified_diff(result.splitlines(), _output.splitlines(),
                                 'Output', 'Expect', lineterm=''):
            print(line)

        if result == _output:
            print("OK")
        else:
            print("NG")

    else:
        main(StringIO(_input))

if __name__ == '__main__':
    test = False
    compare = True
    if test:
        test_main(compare)
    else:
        import sys
        if len(sys.argv) > 1:
            f = open(sys.argv[1])
            main(f)
            f.close()
        else:
            main(sys.stdin)
