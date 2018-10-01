# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 10:17:26 2014

@author: poonna
"""

c = 500.0
f = 4.0
x = 2000.0

def solve(c, f, x):
    rate = 2.0
    time = 0.0
    while True:
        if x <= c:
            time = time + x / rate
            return time
        time = time + c / rate
        if (x-c) / rate < x / (rate+f):
            time = time + (x-c) / rate
            return time
        rate = rate + f

num_tests = int(raw_input())
for i in range(num_tests):
    c, f, x = map(float, raw_input().split())
    print 'Case #' + str(i+1) + ': ' + str(solve(c, f, x))
