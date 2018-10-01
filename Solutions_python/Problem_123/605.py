#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 13 Apr 2013

@author: Artem
'''
from __future__ import division
from math import sqrt
import os
import sys
import time
import math


def write_case(f_out, out, k):
    out = "Case #%d: %s\n" % (k, out)
    f_out.write(out)
    #print out

def solve(f_in, f_out):
    T = f_in.readline()
    if not T:
        print 'The input file is empty!'
        sys.exit()
    T = int(T)
    
    for k in xrange(1, T+1):
        A, N = [int(x) for x in f_in.readline().split()]
        n = [int(x) for x in f_in.readline().split()]
        n.sort()
        print A, n
        
        m = 0
        a = A
        l = len(n)+1
        for i in n:
            l -= 1
            if 2*a-1 > i and a <= i:
                m += 1
                a += a-1 + i
            elif 2*a-1 <= i and a <= i:
                aa = a
                c = 0
                if a != 1:
                    while aa <= i:
                        aa += aa-1
                        c += 1
                else:
                    c = float('inf')
                if c < l:
                    a = aa + i
                    m += c
                else:
                    m += 1
            else:
                a += i
                
        out = m
        write_case(f_out, out, k)
        
        print a, m

def main():
    START = time.time()
    my_dir = os.getcwd()
    name = os.path.basename(__file__)[:-3:]
    
    file_in = "%s\\input\\%s.in" % (my_dir, name)
    file_out = "%s\\output\\%s.out" % (my_dir, name)
    with open(file_in, 'a+') as f_in:
        with open(file_out, 'w') as f_out:
            solve(f_in, f_out)
    
    print 'All done in %f s' % (time.time()-START)
    
if __name__ == '__main__':
    main()