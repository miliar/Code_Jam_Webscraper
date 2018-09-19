#!/usr/bin/python
from math import sqrt


def palindrome(num):
    return str(num) == str(num)[::-1]
    
def everything(r):
    r = int(r)
    nums = raw_input().split(" ")
    
    minv = int(nums[0])
    maxv = int(nums[1])

    counter = 0
    for i in range(minv, maxv+1):
        if sqrt(i) - int(sqrt(i)) == 0:
            numsqrt = int(sqrt(i))    
            if (palindrome(i) == True) and (palindrome(numsqrt) == True):
                counter = counter + 1
    return counter                
    
          
            
cases = int(raw_input())

L = []
M = []

for r in range(cases):
    #everything(r)
    L.append(everything(r))
    M.append(r)
    
for x in range(len(L)):
    r = M[x]
    print "Case #%d: %d" % (r+1, L[x])
