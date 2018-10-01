import sys
from pprint import pprint

def add(fs, d):
    r = 0
    ds = d[1:].strip().split('/')
    for d in ds:
        if not fs.has_key(d):
            fs[d] = {}
            r += 1
        fs = fs[d]
    return r

T = int(sys.stdin.readline())

for casenum in xrange(1, T+1):
    n, m = map(int, sys.stdin.readline().split())
    solution = 0
    if casenum == 56:
        print n, m
    fs = {}
    for i in xrange(n):
        d = sys.stdin.readline()
        add(fs, d)
    for i in xrange(m):
        d = sys.stdin.readline()
        solution += add(fs, d)
        
    #print "Case #%d: %d" % (casenum, solution)