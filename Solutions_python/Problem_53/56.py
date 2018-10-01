#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def processFile(fname):
    def processCase(f):
        n, k = f.readline().strip("\n").split(" ")
        k = int(k)
        i = i_ = 2 ** int(n);
        while (i < k):
            i *= 2
        while (i > k):
            i -= i_
        i += i_
        i -= 1
        if i == k:
            return "ON"
        return "OFF"
    
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

#processFile("test.in")
#processFile("sample.txt")
#processFile("A-small-attempt0.in")
processFile("A-large.in")
