#!/usr/bin/env python

from sys import *
from math import *

def processCase(trees, case):
    num = 0
    
    for p1 in trees:
        for p2 in trees:
            for p3 in trees:
                if p1 != p2 and p1 != p3 and p2 != p3:
                    x = float (p1[0] + p2[0] + p3[0]) / 3
                    y = float (p1[1] + p2[1] + p3[1]) / 3
                    if abs(x - round(x)) < 0.001 and abs(y - round(y)) < 0.001:
                        num += 1
        
    print "Case #%d: %d" % (case, num / 6)    
    return

def process(lines):
    N = int (lines[0])
    case = 1
    i = 1
    while case <= N:        
        (n, A, B, C, D, x0, y0, M) = lines[i].strip("\r\n").split(' ')
        i += 1
        
        x = int (x0)
        y = int (y0)
        trees = [(x, y)]
        for j in range(1, int (n)):
            x = (int (A) * x + int (B)) % int (M)
            y = (int (C) * y + int (D)) % int (M)
            trees.append((x, y))
            
        processCase(trees, case)
        case += 1
        

def usage():
    print "Usage %s input" % argv[0]

def main():    
    if len(argv) < 2:
        usage()
        exit()
        
    input = argv[1]
    f = open(input, 'r')
    
    try:
        lines = f.readlines()
        process(lines)
        
    finally:
        f.close()

if __name__ == '__main__':
    main()