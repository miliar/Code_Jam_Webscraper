#!/usr/bin/python


import sys
from itertools import izip
from math import sqrt


def check_p(i):
    s = "%d" % i
    for i in xrange(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
    
def main():
    for i in xrange(1, 1001):
        i_s = int(sqrt(i))
        if i_s ** 2 == i:
            if check_p(i) and check_p(i_s):
                print "%d," % i, 

if __name__ == '__main__':
    main()
    