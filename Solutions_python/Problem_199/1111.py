#!/usr/bin/env python3
import sys

class MyOutput:

    def __init__(self):
        self.__count = 1

    def out(self, s):
        print("Case #{}: {}".format(self.__count, s))
        self.__count += 1
        

def parse_row(text):
    rrow, rk = text.split()
    k = int(rk)
    row = []
    for c in rrow:
        if c == '-':
            row.append(0)
        else:
            row.append(1)
    return row, k

def flip(row, i, k):
    for j in range(k):
        row[i+j] = 1 if row[i+j] == 0 else 0

def solve(row, k):
    count = 0
    i = -1
    while(True):
        # Search for next 0
        try:
            i = row.index(0, i+1)
        except ValueError:
            # no 0 found we are good
            return count
    
        if i > len(row)-k:
            # The last 0 is too far -> no solution
            return -1
    
        flip(row, i, k)
        count += 1

def process(fd):
    count = int(fd.readline())
    myout = MyOutput()
    for i in range(count):
        row, k = parse_row(fd.readline())
        res = solve(row, k)
        s = "IMPOSSIBLE" if res == -1 else str(res)
        myout.out(s)

def main(fname):
    with open(fname) as fd:
        data = process(fd)

def test():
    main("test.in")

main(sys.argv[1])
