#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:05:16 2017

@author: ansli
"""


def tidy(n):
    lst = [int(x) for x in n]
    for index in range(0, len(lst) - 1):
        if lst[index] > lst[index + 1]:
            for left in range(index + 1, len(lst)):
                lst[left] = 9
            lst[index] -= 1
            for back in range(index, 0, -1):
                if lst[back] < lst[back - 1]:
                    lst[back] = 9
                    lst[back - 1] -= 1
    while lst[0] == 0:
        lst = lst[1:]
                
    return ''.join([str(i) for i in lst])
    

totalCase = int(raw_input())  # read a line with a single integer
for case in xrange(1, totalCase + 1):
    n = raw_input()
    result = tidy(n)
    print "Case #{}: {}".format(case, result)
