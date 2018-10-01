#!/usr/bin/env python
def memoize(f):
    memo = {}
    def inner(n, k):
        if (n, k) in memo:
            return memo[(n, k)]
        else:
            res = f(n, k)
            memo[(n, k)] = res
            return res
    return inner

@memoize
def neighbors(n, k):
    if k <= 1:
        return n - k
    if n % 2 == 0: # n is even
        if k % 2 == 0: # k is even
            return min(neighbors(n/2-1, k/2-1), neighbors(n/2, k/2))
        else: # k is odd
            return min(neighbors(n/2-1, k/2), neighbors(n/2, k/2))
    else: # n is odd
        return neighbors(n/2, k/2)

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        n, k = raw_input().split(" ")
        res = neighbors(int(n), int(k))
        L = (res + 1) / 2
        R = res / 2
        print "Case #{}: {} {}".format(i, L, R)
