#!/usr/bin/env python

"""Google Code Jam 2010, Round 1B, A."""

__author__ = "Samuel Spiza"

import sys
import math

#FILE_NAME = "A-practice.in"
#FILE_NAME = "A-small-attempt0.in"
FILE_NAME = "A-large.in"

cnt = 0

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
    n, m = 0, 0
    cases = []
    for line in lines[1:]:
        if n == 0 and m == 0:
            n, m = [int(x) for x in line.strip().split()]
            cases.append([[],[]])
        elif n == 0:
            cases[-1][1].append(line.strip())
            m -= 1
        else:
            cases[-1][0].append(line.strip())
            n -= 1
    return N, cases

def do(case):
    global tree
    tree = {}
    for i in range(len(case[0])):
        tree = inc(case[0][i], tree)
    before = cnt(0, tree)
    for i in range(len(case[1])):
        tree = inc(case[1][i], tree)
    after = cnt(0, tree)
    return after-before

def inc(s, tree):
    if s == "":
        return tree
    parts = s.split("/")
    new = ""
    if 2 < len(parts):
        new = "/" + "/".join(parts[2:])
    if parts[1] in tree:
        tree[parts[1]] = inc(new, tree[parts[1]])
    else:
        tree[parts[1]] = inc(new, {})
    return tree
    
def cnt(i, tree):
    if len(tree) == 0:
        return i
    else:
        for key in tree:
            i = cnt(i + 1, tree[key])
    return i

if __name__ == "__main__":
    sys.exit(main())
