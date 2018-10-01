#!/usr/bin/python

import os
import sys
import math
import fractions

infile = open(sys.argv[1])

line_num = int(infile.readline())

for i in range(line_num):
    line = infile.readline()
    items = line.split(' ')
    nums = [int(x) for x in items]
    nums = nums[1:]
    nums = list(set(nums))
    nums.sort()
    diff = []
    for j in range(1, len(nums)):
        diff.append(nums[j] - nums[j - 1])
    step = diff[0]
    for j in range(1, len(diff)):
        step = fractions.gcd(step, diff[j])
    init = int(math.ceil(min(nums) / float(step)) * step) - min(nums)
    #print >>sys.stderr, i, init, step, '---', nums
    while init < 0:
        init += step
    while True:
        p = True
        for ii in nums:
            if (ii + init) % step != 0:
                p = False
                break
        if p == True:
            print 'Case #' + str(i + 1) + ':', str(init)
            break
        init += step

    
