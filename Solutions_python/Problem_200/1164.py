#!/usr/bin/env python3
import sys

class MyOutput:

    def __init__(self):
        self.__count = 1

    def out(self, s):
        print("Case #{}: {}".format(self.__count, s))
        self.__count += 1
        

def parse_line(l):
    return int(l)

def solve(n):
    org = n
    
    while(True): # We return when finding a solution
        # 1-digit number special case
        if n < 10:
            return n

        # finding first digit < than previous
        ns = str(n)
        prev = ns[0]
        for i,d in enumerate(ns[1:], 1):
            if d >= prev:
                prev = d
            else:
                break
    
        if d == prev: # We won
            return n
        else:
            # ns[:i] has to be decremented
            # ns[i:] has to be toggled to [9..]
            n = n - int(ns[i:]) - 1
    

def process(fd):
    count = int(fd.readline())
    myout = MyOutput()
    for i in range(count):
        n = parse_line(fd.readline())
        res = solve(n)
        myout.out(str(res))

def main(fname):
    with open(fname) as fd:
        data = process(fd)

def test():
    main("test.in")

main(sys.argv[1])

