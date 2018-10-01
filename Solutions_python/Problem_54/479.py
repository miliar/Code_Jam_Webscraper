#!/usr/bin/env python

import sys
from pdb import set_trace as st
def main():
    f = open(sys.argv[1], "r")
    T = int(f.readline().strip())
    c = 1
    while(c <= T):
        a = 0
        l = f.readline().strip()
        nums_str = l.split(' ')[1:]
        nums = [ int(x) for x in nums_str]
        nums.sort()
        s = len(nums)
        prev = int(nums[0])
        gd = nums[1] - nums[0] #  assert(gd != 0)
        for i in xrange(1, s):
            curr = nums[i]
            d = curr - prev
            gd = gcd(gd, d)
            prev = curr

        k = (nums[0] / gd) * gd
        while (k < nums[0]):
            k += gd
        a = k - nums[0]
        print("Case #%d: %d" % (c,a))
        c += 1

def gcd(a, b):
    while(a):
        a, b = (b%a, a)
    return b

if __name__ == "__main__":
    main()
