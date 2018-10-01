#!/usr/bin/python

import sys
import re

def alien_match(pattern, words):
    count = 0
    for word in words:
        pattern = pattern.replace('(','[').replace(')',']')
        if re.match(pattern, word):
            count+=1
    return count



n = sys.stdin.readline().strip().split(" ")
words = []
for i in range(int(n[1])):
    words += [sys.stdin.readline().strip()]

for i in range(int(n[2])):
    pattern = sys.stdin.readline().strip()
    print "Case #%s: %s" % (i+1, alien_match(pattern, words))






