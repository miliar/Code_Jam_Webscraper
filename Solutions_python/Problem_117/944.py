#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import numpy as np

def solve(array, lines, columns):
    max_lines = [max(line) for line in array]
    max_columns = [max(line) for line in array.T]
    
    for line in xrange(lines):
        for column in xrange(columns):
            n = array[line][column]
            if n < max_lines[line] and n < max_columns[column]:
                return 'NO'

    return 'YES'


def main():
    for case in xrange(int(sys.stdin.readline().strip())):
        lines, columns = map(int, sys.stdin.readline().strip().split(' '))
        array = []
        for line in xrange(lines):
            array.append(map(int, sys.stdin.readline().strip().split(' ')))
        print 'Case #%d: %s' % (
            case + 1,
            solve(np.array(array), lines, columns)
        )

    return 0

if __name__ == '__main__':
    sys.exit(main())
