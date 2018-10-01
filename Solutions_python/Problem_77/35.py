#!/usr/bin/python

import sys
import math

S = {}
def stirling(n, k):
    global S
    if S.has_key((n,k)):
        return S[(n,k)]
    f = math.factorial
    enu = 0
    for i in range(n-k+1):
        kk = 1
        if i % 2 == 1:
            kk = -1
        if i > 8:
            break
        enu = enu + 1.0 * kk/f(i)
    denum = f(k)
    result = 1.0 * enu / denum
    S[(n, k )] = result
    return result

X = { 0: 0,
      1: 0,
      2: 2
      }
def x(n):
    return n
    global X
    if X.has_key(n):
        return X[n]
    else:
        denum = 1 - stirling(n, 0)
        enu = 1
        for i in range(1, n+1):
            enu = enu + stirling(n, i) * x(n - i)
        result = 1.0 * enu / denum
        X[n] = result
        return result

def goro(sorted_arr, arr):
    n = 0
    for i in range(len(arr)):
        if arr[i] == sorted_arr[i]:
            continue
        else:
            n = n + 1
    return x(n)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        f.readline()
        arr = map(lambda x: int(x), f.readline().strip().split())
        sorted_arr = list(arr)
        sorted_arr.sort()
        result = goro(sorted_arr, arr)
        print "Case #%d: %s" % (i + 1, result)
        
if __name__ == "__main__":
    sys.exit(main())

