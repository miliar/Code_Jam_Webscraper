#!/usr/bin/env python
#coding: utf-8

__author__ = "Pedro Pérez Sánchez <pedropobla@gmail.com>"

import sys
import math

if __name__ == '__main__':
    T = int( sys.stdin.readline() )
    for i in range(T):
        [r,t] = [int(x) for x in sys.stdin.readline().split()]
        rings = 0
        while(t>=(r+1)*(r+1)-r*r):
            rings += 1
            t -= (r+1)*(r+1)-r*r
            r += 2
        print "Case #"+ str(i+1) +": "+ str(rings)
    exit(0)