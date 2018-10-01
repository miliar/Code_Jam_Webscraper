#!/usr/bin/env python

import math
import sys

def is_fair(n):
    n = str(n)
    m = n[::-1]
    flag = True
    for i in range(0, len(n)):
        if m[i] != n[i]:
            flag = False
            break
    return flag

def is_square(n):
    ns = math.sqrt(n)
    if int(ns) * int(ns) == n:
        return True
    else:
        return False

input = open(sys.argv[1], "r")
cases = int(input.readline().strip())
for i in range(0, cases):
    a, b = input.readline().strip().split(" ")
    a, b = int(a), int(b)
    counter = 0
    for j in range(a, b+1):
        if is_fair(j) and is_square(j) and is_fair(int(math.sqrt(j))):
            counter += 1
    print "Case #%d: %d" % (i+1, counter)