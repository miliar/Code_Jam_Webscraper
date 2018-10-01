#!/usr/bin/env python

import copy

def solve(N, x, y):
    sum = 0
    while len(x) > 0:
        sum += min(x) * max(y)
        x.remove(min(x))
        y.remove(max(y))
    
    return sum

def solve_problem(fname):
    l = [line.strip() for line in open(fname).readlines()]

    n_problems = int(l.pop(0).strip())

    n = 1
    while n_problems > 0:
        N = int(l.pop(0))
        x = [int(i) for i in l.pop(0).split()]
        y = [int(i) for i in l.pop(0).split()]

        print 'Case #%d: %d' % (n, solve(N, x, y)) 
        n = n + 1
        n_problems = n_problems - 1

if __name__ == '__main__':
    solve_problem('input.txt')
