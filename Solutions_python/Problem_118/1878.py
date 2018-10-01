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


def write_case(f_out, out, k):
    out = "Case #%d: %s\n" % (k, out)
    f_out.write(out)
    #print out

def check(n):
    sn = str(n)
    l = len(sn)//2
    if len(sn) % 2 == 0:
        if sn[:l:] == sn[:l-1:-1]:
            return True
        else:
            return False
    else:
        if sn[:l:] == sn[:l:-1]:
            return True
        else:
            return False
    
    return False

def solve(f_in, f_out):
    T = f_in.readline()
    if not T:
        print 'The input file is empty!'
        sys.exit()
    T = int(T)
    
    for k in xrange(1, T+1):
        A, B = [int(x) for x in f_in.readline().split()]
        a = int(round(sqrt(A)))
        b = int(round(sqrt(B)))
        if a**2 < A:
            a += 1
        if b**2 > B:
            b -= 1
        out = 0
        for n in xrange(a, b+1):
            if check(n):
                if check(n**2):
                    out += 1
        #print A, B, a, b, out
        
        write_case(f_out, out, k)

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