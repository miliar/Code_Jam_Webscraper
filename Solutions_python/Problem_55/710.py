#! /usr/bin/env python
import sys

def profit(R, K, N, g):
    last_n, p = 0, 0
    for r in xrange(R):
        k = 0
        for n in xrange(last_n, N + last_n):
            if k + g[n % N] <= K:
                k += g[n % N]
            else:
                last_n = n
                break
        p += k
    return p

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "too few arguments"

    input = open(sys.argv[1], "r").readlines()

    T = int(input[0])

    for i in xrange(1, 2*T, 2):
        R, k, N = map(int, input[i].split())
        print "Case #%d: %d" % (i // 2 + 1, profit(R, k, N, map(int, input[i+1].split())))
