#!/usr/bin/python
# -*- coding: utf-8 -*-

# A cheap implementation for the small data set :)

import math

def isFair(x):
    s = str(int(x))
    for i in xrange(len(s)/2):
        if not s[i] == s[-(i+1)]:
            return False
    
    return True;

def isSquare(x):
    rt = int(math.sqrt(x))
    if (x == (rt*rt)) and isFair(rt):
        return True
    else:
        return False

def main():
    in_file = open("C-small-attempt0.in", mode='r')
    out_file = open("C-small-attempt0.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    for i in xrange(T):
        line = lines[i+1]
        A, B = line.strip().split(' ')
        count = 0
        for x in range(int(A), int(B)+1):
            if isFair(x) and isSquare(x):
                count += 1
                
        out_file.write("Case #" + str(i+1) + ": " + str(count) + "\n") 
        
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()