#!/usr/bin/env python
import math

def isPalindrome(data):
    word = str(data)
    return word == word[::-1]

cnt = 0
num = 0
starts = []
ends = []
for line in open("C-small-attempt0.in"):
    if cnt == 0:
        num = int(line)
    else:
        line = line.strip().split()
        starts.append(int(line[0]))
        ends.append(int(line[1]))
    cnt += 1

for i in range(num):
    start = starts[i]
    end = ends[i]
    newStart = int(math.ceil(math.sqrt(start)))
    newEnd = int(math.floor(math.sqrt(end)))
    cnt = 0
    for j in range(newStart, newEnd+1):
        if isPalindrome(j ** 2) and isPalindrome(j):
            cnt += 1
    print "Case #%d: %d" % (i+1, cnt)
