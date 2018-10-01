#!/usr/bin/env python
import fileinput
import os.path

def main():
    reader = fileinput.input()
    trials = int(reader.next())
    for t in range(1, trials+1):
        result = trial(reader)
        print "Case #%d: %s" % (t, result)

def trial(reader):
    n, m = reader.next().strip().split()
    n = int(n)
    m = int(m)
    existing = {}
    for k in range(n):
        d = reader.next().strip()
        existing[d] = True
    count = 0
    for k in range(m):
        d = reader.next().strip()
        count += mkdir(existing, d)
    return count

def mkdir(existing, d):
    if d in existing or d == '/':
        return 0
    n = mkdir(existing, os.path.dirname(d))
    existing[d] = True
    return n + 1

main()
