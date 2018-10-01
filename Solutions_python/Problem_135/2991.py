#!/usr/bin/env python

import sys


def guess(r1, m1, r2, m2):
    common = list(set(m1[r1 - 1]).intersection(m2[r2 - 1]))
    #print("%s :: %s :: %s" % (common, m1[r1 - 1], m2[r2 - 1]))
    if len(common) == 1:
        return common[0]
    if len(common) == 0:
        return 'Volunteer cheated!'
    if len(common) > 1:
        return 'Bad magician!'


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        matrix1 = []
        matrix2 = []
        row1 = int(infile.readline())
        for j in range(4):
            line = infile.readline().split()
            matrix1.append([])
            matrix1[j] = map(int, line)
        row2 = int(infile.readline())
        for j in range(4):
            line = infile.readline().split()
            matrix2.append([])
            matrix2[j] = map(int, line)

        print 'Case #%s: %s' % (i + 1, guess(row1, matrix1, row2, matrix2))

main(sys.stdin)
