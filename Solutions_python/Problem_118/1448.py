#! /usr/local/bin/python2.7
import sys
import os
import math

def is_fair(num):
    numstr = str(num)
    lenstr = len(numstr)
    for i in range(lenstr // 2):
        if numstr[i] != numstr[lenstr - i - 1]:
            return False
    return True


if len(sys.argv) < 2: sys.exit(-1)
if not os.path.isfile(sys.argv[1]): sys.exit(-2)

f = open(sys.argv[1])

num_inputs = int(f.readline())

for case in range(num_inputs):
    dim = map(int, f.readline().split())
    
    nums = 0
    for i in range(dim[0], dim[1] + 1):
        
        if not is_fair(i): 
            continue

        sqrt = math.sqrt(i)
        if not sqrt.is_integer() or not is_fair(int(sqrt)):
            continue

        nums += 1

    print "Case #%i: %i" % (case + 1, nums)
