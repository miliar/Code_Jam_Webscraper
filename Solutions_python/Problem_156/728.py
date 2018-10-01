#!/usr/bin/env python

def solve():
    n = int(raw_input())
    inputs = []
    for i in xrange(n):
        print 'Case #%d: %d' % (i + 1, solve_single())

def solve_single():
    non_empty = raw_input()
    pancs = map(int, raw_input().split(' '))
    t = 0
    pancs.sort()
    return calculate2(pancs)

def calculate(pancs):
    max_pancs = pancs[-1]
    if max_pancs < 4:
        return max_pancs
    pancs1 = []
    for p in pancs:
        if p > 1:
            pancs1.append(p - 1)
    opt1 = calculate(pancs1)
    pancs2 = list(pancs)
    divided = max_pancs/2
    # if max_pancs % 2 != 0:

    pancs2[-1] = divided
    pancs2.append(max_pancs - divided)
    pancs2.sort()
    opt2 = calculate(pancs2)

    pancs3 = list(pancs)
    return 1 + min(opt1, opt2)

def calculate2(pancs):
    max_pancs = pancs[-1]
    if max_pancs < 4:
        return max_pancs
    opts = []
    pancs1 = []
    for p in pancs:
        if p > 1:
            pancs1.append(p - 1)
    opts.append(calculate(pancs1))
    divided = max_pancs/2
    for i in xrange(1, divided + 1):
        pancsi = list(pancs)
        pancsi[-1] = i
        pancsi.append(max_pancs - i)
        pancsi.sort()
        # if len(pancs) > 1:
        opts.append(calculate(pancsi))

    return 1 + min(opts)





if __name__ == '__main__':
    solve()
