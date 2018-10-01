#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv

def solve(cipher):
    m = int(cipher.split(" ")[0])
    arr = cipher.split(" ")[1:][0]

    total = 0
    count = 0
    for i in range(m+1):
        if (i<=total):
            total += int(arr[i])
        else:
            count +=(i-total)
            total = i
            total += (int(arr[i]))
    return count


filename = argv[1]
File = open(filename)

n = int(File.readline())

with open('answer', 'w') as f:
    for caseNr in xrange(1, n+1):
        cipher = File.readline()
        f.write("Case #%i: %s" % (caseNr, solve(cipher)))
        f.write("\n")

