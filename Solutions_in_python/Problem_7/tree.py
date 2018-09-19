#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scott Patterson
# asp742@gmail.com
#

import sys
from itertools import cycle

def get_trees(n, A, B, C, D, x0, y0, M):
    tree_list = []
    X = x0
    Y = y0
    tree_list.append((X, Y))

    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        tree_list.append((X, Y))

    return tree_list

def div_3(n):
    return sum(n)/3 == 1.0*sum(n)/3.0

def get_tri(trees):
    n = len(trees)
    r = 0

    for x in xrange(n-2):
        for y in xrange(x+1, n-1):
            for z in xrange(y+1, n):
                t = [trees[x], trees[y], trees[z]]
                is_x_3 = div_3([i[0] for i in t])
                if not is_x_3:
                    continue
                is_y_3 = div_3([i[1] for i in t])
                if is_y_3:
                    r += 1
    return r

def main():
    file = sys.argv[1]
    data = (lines.strip() for lines in open(file))

    ncase = int(data.next())
    for case in range(ncase):
        n, A, B, C, D, x0, y0, M = [int(i) for i in data.next().strip().split()]

        trees = get_trees(n, A, B, C, D, x0, y0, M)
        
        print 'Case #%d: %d' % (case + 1, get_tri(trees))

if __name__ == '__main__':
    main()
