#!/usr/bin/python2.7
import sys


def get_res(n, ds):
    mx = max(ds)
    best_res = mx
    for d in xrange(1, mx):
        res = d
        for i in xrange(n):
            if ds[i] > d:
                res += (ds[i] - d + (d - 1)) // d
        best_res = min(best_res, res)
    return best_res


if __name__ == "__main__":
    tcn = int(sys.stdin.readline())
    for tc in range(tcn):
        n = int(sys.stdin.readline())
        d = map(int, sys.stdin.readline().split())
        print "Case #%d: %d" % (tc + 1, get_res(n, d))
