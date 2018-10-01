#!/usr/bin/env python

import sys
import math
import time


def palindrome(number):
    n = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number /= 10
    return n == reverse

sys.stdin = file("c-input")
sys.stdout = file("c-output", "w")

input_count = int(raw_input())
for instance in range(input_count):
    inp = raw_input().split()
    lower = min(int(inp[0]), int(inp[1]))
    upper = max(int(inp[0]), int(inp[1]))

    now = time.time()
    count = 0
    start = int(math.sqrt(lower))
    if start * start < lower:
        start += 1
    end = int(math.sqrt(upper))

    for i in range(start, end + 1):
        # print i, i * i
        if palindrome(i) and palindrome(i * i):
            count += 1

    print "Case #%i: %i" % (instance + 1, count)
    # print "Case #%i: %i (%f)" % (instance + 1, count, time.time() - now)
