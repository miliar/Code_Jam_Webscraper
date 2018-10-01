#!/usr/bin/env python

import sys

NR = 4

input = sys.stdin.read()

lines = input.split('\n')

T = lines.pop(0)

for i in range(1, int(T) + 1):
    #print '-' * 20

    in1 = lines.pop(0)
    #print 'In1: ', in1

    matrix1 = []

    for j in range(NR):
        row = lines.pop(0)
        cols = row.split(' ')
        matrix1.append(cols)
    #print 'Matrix1:'
    #print matrix1

    in2 = lines.pop(0)
    #print 'In2: ', in2

    matrix2 = []

    for j in range(NR):
        row = lines.pop(0)
        cols = row.split(' ')
        matrix2.append(cols)
    #print 'Matrix2:'
    #print matrix2

    row1 = matrix1[int(in1) - 1]
    row2 = matrix2[int(in2) - 1]

    #print 'row1: ', row1
    #print 'row2: ', row2

    num = set(row1) & set(row2)
    
    if len(num) == 1:
        print 'Case #%s: %s' % (i, num.pop()) 
    elif len(num) > 1:
        print 'Case #%s: %s' % (i, 'Bad magician!')
    elif len(num) == 0:
        print 'Case #%s: %s' % (i, 'Volunteer cheated!')
