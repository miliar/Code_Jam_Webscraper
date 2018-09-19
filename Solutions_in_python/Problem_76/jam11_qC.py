#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     08/05/2011
# Copyright:   (c) wani 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys

def num2bin(num):
    if num == 0:
        return []
    if num % 2 == 0:
        return [0] + num2bin(num/2)
    else:
        return [1] + num2bin(num/2)

def fix_bin(a,b):
    if len(a) > len(b):
        return (a,b + [0] * (len(b) - len(a)))
    else:
        return (a + [0] * (len(b) - len(a)),b)

def add_bin(a,b):
    a,b = fix_bin(a,b)
    c = []
    for i in range(len(a)):
        if a[i] == b[i]:
            c.append(0)
        else:
            c.append(1)
    return c

def devide(nums):
    nums.sort()
    max = nums[-1]
    total = [0]
    for num in nums:
        b = num2bin(num)
        total = add_bin(total,b)
    if 1 in total:
        return 0
    else:
        return sum(nums[1:])

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        candies = int(f.readline().strip())
        nums = [int(x) for x in f.readline().strip().split()]
        n = devide(nums)
        if  n== 0:
            out = "Case #%d: NO"%(i+1) + "\n"
        else:
            out = "Case #%d: %d"%(i+1,n) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
