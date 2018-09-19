import sys
from datetime import datetime

f = None
START = datetime.now()

def read_int():
    return int(f.readline())

def read_ints():
    return map(int, f.readline().split())

def read_word():
    return f.readline().strip()

def char_range(start, end):
    return [chr(i) for i in range(ord(start), ord(end) + 1)]

def matrix(rows, cols, value=None):
    return [[value for _ in range(cols)] for __ in range(rows)]


############################################################################

def solve(n, w, l, ds):
    from random import random
    from math import sqrt

    positions = [(0., 0., ds[0])]

    for d in ds[1:]:
        test = None
        while True:
            test = (random()*w, random()*l)
            for x, y, dp in positions:
                delta_x = test[0] - x
                delta_y = test[1] - y
#                print >>sys.stderr, 'D', sqrt(delta_x*delta_x + delta_y*delta_y), (dp + d)
                if sqrt(delta_x*delta_x + delta_y*delta_y) < (dp + d):
                    break
            else:
                break
        positions.append((test[0], test[1], d))


    return ' '.join(['{0} {1}'.format(p[0], p[1]) for p in positions])


def main():
    global f

    with open(sys.argv[1]) as f:
        t = read_int()

        for index in xrange(t):
            print >>sys.stderr, 'Working on case #', index + 1, datetime.now() - START

            n, w, l = read_ints()
            ds = read_ints()

            result = solve(n, w, l, ds)

            print 'Case #{0}: {1}'.format(index + 1, result)


if __name__ == '__main__':
    main()
