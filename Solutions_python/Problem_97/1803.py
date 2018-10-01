#!/usr/bin/env python
import sys

def rshift(i):
    return i[-1] + i[:-1]

def calc_pairs_number(i, a, b):
    ii, p = str(i), 0
    jj = ii
    
    for r in xrange(len(ii) -1):
        jj = rshift(jj)
        j = int(jj)
        
        if j == i or jj[0] == '0':
            continue
        
        if j >= a and j <= b:
            p = p + 1
            print i, r, jj

    return p

def calc_pairs(a, b):
    if len(b) == 1: return 0

    a, b, p = int(a),  int(b), 0
    for i in xrange(a, b+1):
        p = p + calc_pairs_number(i, a, b)
        
    return p / 2


if __name__ == '__main__':
    inputs = open(sys.argv[1]).readlines()
    outputs = open(sys.argv[2], "w")

    for i, line in enumerate(inputs):
        if i != 0:
            line = line.strip().split()
            output = "Case #%s: %s\n" % (i, calc_pairs(line[0], line[1]))
            outputs.write( output )
            
            print "%20s, %s" % (line,  output.strip())
    
