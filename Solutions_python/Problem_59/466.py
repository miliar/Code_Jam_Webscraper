#!/usr/bin/env python

import re
import os
import sys
import time
from copy import copy
from itertools import *
import os.path as path

try:
    import psyco
    psyco.full()
except:
    pass

def readint():
    return int(raw_input())

def readfloat():
    return float(raw_input())

def readlinearray(function):
    return map(function, raw_input().split())

def do_it(already = [], directory = None):
    if directory in already:
        return 0
    already.append(directory)
    return 1 + do_it(already, path.dirname(directory))

def main():
    T = readint()
    for count in range(T):
        N, M = readlinearray(int)
        mkdir = 0
        already = []
        already.append('/')
        new_dirs = []
        for input_ in range(N):
            already.append(raw_input())
        for input_ in range(M):
            new_dirs.append(raw_input())
        for directory in new_dirs:
            mkdir += do_it(already, directory)
        print 'Case #' + str(count + 1) + ':',
        print mkdir

if __name__ == '__main__':
    main()

