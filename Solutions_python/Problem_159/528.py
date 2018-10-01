import math

inp = open("in.txt")
out = open("out.txt", "w+")

def write_case(index, result):
    out.write("Case #%d: %s\n" % (index+1, result))

cases = int(inp.readline())  

def solve_case():
    n = int(inp.readline())
    a = [int(x) for x in inp.readline().split()]
    if n == 1:
        return "0 0"
    
    maxdif = 0
    mineaten = 0
    for i in xrange(1, n):
        dif = a[i-1] - a[i]
        if dif > 0:
            mineaten += dif
            maxdif = max(maxdif, dif)
    
    eaten2 = 0
    for i in xrange(0, n-1):
        eaten2 += min(a[i], maxdif)
    
    return "%s %s" % (mineaten, eaten2)

for i in xrange(cases):
    print "case %s" % (i+1)
    write_case(i, solve_case())