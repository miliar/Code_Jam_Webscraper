#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# const
F_V = 0x01
F_H = 0x02

class RowDirection(object):
    def get_1st(self, x, y, field):
        return (None, None)
    def get_next(self, x, y, field):
        return (None, None)

class Vertical(RowDirection):
    def get_1st(self, x, y, field):
        return (x, 0)
    def get_next(self, x, y, field):
        return (x, y+1) if y+1 <= len(field)-1 else (None, None)

class Horizontal(RowDirection):
    def get_1st(self, x, y, field):
        return (0, y)
    def get_next(self, x, y, field):
        return (x+1, y) if x+1 <= len(field[y])-1 else (None, None)

def check(field, flags, x, y, rd):
    result = True
    (i, j) = rd.get_1st(x, y, field)
    while i is not None and j is not None:
        if field[j][i] != field[y][x]:
            result = False
        (i, j) = rd.get_next(i, j, field)
    return result

def doit(field):
    flags = [[0 for j in range(len(field[i]))] for i in range(len(field))]
    for y in range(len(field)):
        for x in range(len(field[i])):
            if field[y][x] == '1':
                if not check(field, flags, x, y, Vertical()) and \
                    not check(field, flags, x, y, Horizontal()):
                    return False
    return True

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (h, w) = map(int, f.readline().split())
        field = [None]*h
        for j in range(len(field)):
            field[j] = f.readline().rstrip().split()
        answer = 'YES' if doit(field) else 'NO'
        print "Case #%d: %s" % (i+1, answer)

