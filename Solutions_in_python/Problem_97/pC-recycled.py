#!/usr/bin/env python
'''
Juan Manuel Caicedo
cavorite.com
'''

import sys

def count_recycled(a, b):
    seen = set()
    n = 0
    len_s = len(str(a))
    if len_s < 2:
        return 0

    for num in xrange(a, b+1):
        s = str(num)
        i = len_s
        while i > 0:
            i -= 1
            rotated = s[i - len_s:] + s[:i]
            n_rot = int(rotated)

            if n_rot < a or n_rot == num or n_rot > b:
                continue

            seen.add(tuple(sorted([num, n_rot])))

    return len(seen)


def main():
    lines = sys.stdin

    cases = int(lines.next())

    for i in xrange(1, cases+1):
        a, b = lines.next().split()
        a = int(a)
        b = int(b)
        n = count_recycled(a, b)
        print 'Case #%d: %s' % (i, n)

if __name__ == '__main__':
    main()
