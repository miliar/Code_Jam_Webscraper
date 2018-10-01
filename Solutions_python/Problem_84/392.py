#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(R, C, pict):
    IMP = ["Impossible"]
    
    for y in range(R):
        for x in range(C):
            if pict[y][x] == "#":
                val = check_and_replace(pict, x, y, C, R)
                if not val:
                    return IMP
                else:
                    pict = val
    
    return pict

def check_and_replace(pict, x, y, C, R):
    if x + 1 >= C or y + 1 >= R:
        return False
    
    pict[y][x] = "/"
    if pict[y][x+1] != "#":
        return False
    pict[y][x+1] = "\\"
    if pict[y+1][x] != "#":
        return False
    pict[y+1][x] = "\\"
    if pict[y+1][x+1] != "#":
        return False
    pict[y+1][x+1] = "/"
    return pict

            

def out(output, msg):
    print(msg)
    output.write(msg + "\n")

#
# main
#
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "sample.in"

with open(file, "r") as f:
    with open(file + ".output", "w") as output:
        T = int(f.readline())
        for n in range(1, T+1):
            R, C = [int(x) for x in f.readline().split()]
            pict = []
            for i in range(R):
                pict.append([x for x in f.readline().rstrip()])
                
            # print(R, pict)
            result = solve(R, C, pict)
    
            out(output, "Case #%d:" % n)
            for row in result:
                s = "".join(row)
                out(output, s)
