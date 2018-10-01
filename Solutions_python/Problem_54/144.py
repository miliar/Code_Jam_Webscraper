#!/usr/bin/env python

import sys
fin = sys.stdin

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    T = int(fin.readline())
    for t in xrange(T):
        N, v = fin.readline().split(" ", 1)
        N, v = int(N), map(int, v.split())

        GCD = reduce(gcd,
            (a - b for a in v for b in v
            if a > b))

        diff = (GCD - v[0] % GCD) % GCD
        print "Case #%d: %s" % (t + 1, diff if True else "OFF")
    return 0

if __name__ == "__main__":
    main()
