from pprint import pprint
import sys
from fractions import gcd

def solveCase(c, f, o):
    line = [int(x) for x in f.readline().strip().split()]
    N = line.pop(0)
    t = line
    t.sort()
    t0 = t.pop(0)
    td = [ti - t0 for ti in t]
    #print "td have", len(td), td
    g = td.pop(0)
    while td:
        g = gcd(g, td.pop(0))
    #print "g found:", g
    if g == 1:
        y = 0
    else:
        if (t0 % g) == 0:
            y = 0
        else:
            target = ((t0 // g) + 1) * g
            y = target - t0
    
    o.write("Case #%d: %s\n" % (c, y))

if __name__ == '__main__':
    input = sys.argv[1]
    f = open(input, 'rb')
    o = open(input.split(".")[0] + "-out" + ".txt", 'wt')
    cases = int(f.readline())
    for c in xrange(cases):
        solveCase(c+1, f, o)
    f.close()
    o.close()
