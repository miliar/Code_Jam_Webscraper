import sys
import re

def line(f):
    return map(int,f.readline().split(" "))

def count_cases(case,words):
    r = re.compile(case.replace("(","[").replace(")","]"))
 
    count = 0
    for w in words:
        if r.match(w):
            count += 1
    return count

def solve(f):
    [L,D,N] = line(f)
    words = [f.readline() for i in range(D)]
    cases = [f.readline() for i in range(N)]

    i = 1
    for c in cases:
        print "Case #%d: %d" % (i,count_cases(c,words))
        i = i+1

solve(sys.stdin)
