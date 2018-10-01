#!/usr/bin/env python
# -*- coding: utf-8

def solve(n, k):
    o = [0, n+1]
    l, r = 0, 0
    for i in xrange(k):
        space = -1 
        p = 0
        for j in xrange(len(o) - 1):
            if o[j+1] - o[j] > space:
                space = o[j+1] - o[j]
                p = j

        avg = (o[p] + o[p + 1]) / 2
        if i < k - 1:
            o.insert(p+1, avg)
        else:
            l = avg - o[p] - 1
            r = o[p+1] - avg - 1

    return max(l, r), min(l, r)

def main():
    T = int(raw_input())
    for i in xrange(T):
        N, K = raw_input().split(" ")
        ma, mi = solve(int(N), int(K))
        print 'Case #{}: {} {}'.format(i + 1, ma, mi)

if __name__ == '__main__':
    main()
