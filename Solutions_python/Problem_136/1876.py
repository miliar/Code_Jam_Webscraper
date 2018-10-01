import sys

def mintime(c, f, x):
    rate = 2
    baset = 0
    mintime = x/rate
    baset += c/rate
    rate += f
    newmin = baset + x/rate
    while newmin<mintime:
        mintime = newmin
        baset += c/rate
        rate += f
        newmin = baset + x/rate
        
    return mintime

n = int(sys.stdin.readline())
for i in range(1,n+1):
    c, f, x = (float(val) for val in sys.stdin.readline().split())
    print "Case #%s: %s" % ( i, mintime(c, f, x) )
