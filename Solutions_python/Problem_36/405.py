#!/usr/bin/python

import sys
import re

WELCOME = "welcome to code jam"

def count(needle, haystack):
    if len(needle) == 1:
        return haystack.count(needle)
    c = needle[0]
    sum = 0
    for i in xrange(len(haystack)):
        if haystack[i] == c:
            sum += (count(needle[1:],haystack[i+1:]) % 1000)
    return sum
    

N = int(sys.stdin.readline())
for i in xrange(N):
    print "Case #%d: %04.d" % (i+1, count(WELCOME,sys.stdin.readline().strip()))
