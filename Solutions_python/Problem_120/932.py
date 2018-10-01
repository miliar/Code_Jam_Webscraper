from decimal import *

def solve(r,t):
 se = 2*r -1
 x = (Decimal(-se) + Decimal(se**2+8*t).sqrt())/Decimal(4)
 return x

T = int(raw_input())
i = 1
while i <= T:
    r, t = [int(j) for j in raw_input().split(" ")]
    print "Case #%d: %d" % (i, int(solve(r,t)))
    i += 1


