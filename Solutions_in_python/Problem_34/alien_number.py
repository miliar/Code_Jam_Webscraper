#!/usr/bin/env python

# N
# alien_number source_language target_language
# ...
# alien_number source_language target_language

import sys
import re


line = sys.stdin.readline()
line = line.split(" ")
l = int(line[0])
d = int(line[1])
n = int(line[2])

dic = {}
i = 0
for line in sys.stdin:
    word = line.rstrip("\n")
    i = i + 1
    dic[word] = word
    if i >= d:
        break

i = 1
for line in sys.stdin:
    word = line.rstrip("\n")
    j = 0
    word = word.replace('(', '[').replace(')', ']')
    for n in dic.iteritems():
        m = re.match(word, n[1])
        if m:
            j = j + 1
    print "Case #%d: %d" % (i, j)
    i = i + 1
