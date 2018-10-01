import sys
from fractions import gcd

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    possible = False
    (n, p_d, p_g) = [int(x) for x in f.readline().split()]
    x = gcd(p_d, 100)
    if 100 / x <= n:
        if p_g == 0 and p_d != 0:
            possible = False
        elif p_g == 100 and p_d != 100:
            possible = False
        else: 
            possible = True
    if possible:
        print "Case #%d: Possible" % (case + 1)
    else:
        print "Case #%d: Broken" % (case + 1) 
