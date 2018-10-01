#!/usr/bin/env python
import re

L, D, N = map(int, raw_input().split())

words = []

for i in xrange(D):
    words.append(raw_input().strip())

patterns = []

for i in xrange(N):
    patterns.append(raw_input().strip())

for i in xrange(N):
    patterns[i] = patterns[i].replace('(', '[').replace(')', ']')

for i in xrange(N):
    num = 0
    for word in words:
        if re.match(patterns[i], word) is not None:
            num += 1
    print "Case #" + str(i+1) + ": " + str(num)
