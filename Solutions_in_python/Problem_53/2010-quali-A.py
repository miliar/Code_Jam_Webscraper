#!/usr/bin/env python

"""Google Code Jam 2010, Qualification Round, A."""

__author__ = "Samuel Spiza"

import sys
import math

#FILE_NAME = "A-practice.in"
#FILE_NAME = "A-small-attempt0.in"
FILE_NAME = "A-large.in"

def main():
    inputFile = open(FILE_NAME, "r")
    N, cases = getCases(inputFile.readlines())
    inputFile.close()
    
    results = [do(case) for case in cases]

    string = "\n".join(["Case #%s: %s" % (z+1, results[z]) for z in range(N)])
    
    print string
    file = open(FILE_NAME.rsplit(".", 1)[0] + ".out", "w")
    file.write(string.strip())
    file.close()

    return 0

def getCases(lines):
    N = int(lines[0].strip())
    cases = []
    for line in lines[1:]:
        cases.append([int(x) for x in line.strip().split()])
    return N, cases

def do(case):
    if (case[1] + 1)%(2**case[0]) == 0:
        return "ON"
    else:
        return "OFF"

    
if __name__ == "__main__":
    sys.exit(main())
