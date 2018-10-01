#!/usr/bin/python
# -*- coding: utf-8 -*-
#
def solve(input):
    max_shy, shy_array = input.split(" ")
    curr = 0
    needed = 0
    for n in xrange(int(max_shy)+1):
        if curr < n:
            needed += n - curr
            curr = n
        curr += int(shy_array[n])
    return needed

if __name__ == "__main__":
    T = input()
    for n in xrange(1, T+1):
        input = raw_input()
        print ("Case #{no}: {result}".format(no=n, result=solve(input)))
