#!/usr/bin/env python
# coding=utf-8

import sys

def win(list):
    s = ''.join(sorted(list))
    if s == 'TXXX' or s == 'XXXX':
        return 'X'
    elif s == 'OOOT' or s == 'OOOO':
        return 'O'
    else:
        return '.'

def solve(grid):
    w = '.'

    for line in grid:
        w = win(list(line))
        if w != '.': return w

    for i in xrange(4):
        w = win([grid[j][i] for j in xrange(4)])
        if w != '.': return w

    w = win([grid[j][j] for j in xrange(4)])
    if w != '.': return w

    w = win([grid[3-j][j] for j in xrange(4)])
    if w != '.': return w

    if w == '.':
        if '.' not in ''.join(grid): return '-'
        else: return '.'

def translate(c):
    if c == 'X' or c == 'O':
        return '%s won' % c
    elif c == '.':
        return 'Game has not completed'
    else:
        return 'Draw'

def main():
    with open(sys.argv[1]) as f:
        T = int(f.readline().strip())
        for i in xrange(T):
            grid = []
            for j in xrange(4):
                l = f.readline().strip()
                grid.append(l)
            f.readline()
            res = solve(grid)
            print 'Case #%d: %s' % (i+1, translate(res))

if __name__ == "__main__":
    main()
