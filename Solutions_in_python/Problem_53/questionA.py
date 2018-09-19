#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import itertools
#import pygraph
#from pygraph.classes.graph import graph


def solve(n,k):
    snapper = []
    for i in xrange(n):
        snapper.append(-1)
    for i in xrange(k):
        #print snapper
        temp = snapper[:]
        temp[0] *= -1
        j = 1
        while j < len(snapper) and snapper[j-1] != -1:
            temp[j] *= -1
            j += 1
        snapper = temp
    #print snapper
    result = ''
    if sum(snapper) == len(snapper): result = 'ON'
    else: result = 'OFF'
    return result

def main():
    #max recursion limit
    sys.setrecursionlimit(sys.maxint)
    input = open('inputs.txt', 'rU')
    output = open('outputs.txt', 'w')
    N = int(input.readline())
    i = 1;
    while i <= N:
        line = input.readline()
        values = line.split()
        n = long(values[0])
        k = long(values[1])
        result = solve(n,k)
        print 'Case #%d: ' % (i) + str(result)
        output.write('Case #%d: ' % (i) + str(result) + '\n')
        i += 1
    input.close()
    output.flush()
    output.close()
    return 0

if __name__ == '__main__':
    main()
