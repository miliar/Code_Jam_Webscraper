#!/usr/bin/python

import re
import sys
from math import floor, ceil

input_file = open('B-large.in')
output_file = open('B-large.out', 'w')

T = int(input_file.readline())

def hok(lawn, row, col, M):
    l = lawn[row][col]
    for i in xrange(M):
        if i != col:
            if lawn[row][i] > l:
                return False
    return True

def vok(lawn, row, col, N):
    l = lawn[row][col]
    for i in xrange(N):
        if i != row:
            if lawn[i][col] > l:
                return False
    return True

def check(lawn, N, M):
    for i in xrange(N):
        for u in xrange(M):
            if not hok(lawn, i, u, M) and not vok(lawn, i, u, N):
                return 'NO'
    return 'YES'


for t in range(T):
    
    
    [N, M] = map(int, input_file.readline().split(' '))
    lawn = []
    for i in xrange(N):
        lawn.append(map(int, input_file.readline().split(' ')))
        
    result = check(lawn, N, M)
    
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")

input_file.close()
output_file.close()
