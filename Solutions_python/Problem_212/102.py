import math, collections, copy, sys
from decimal import Decimal
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, P = [int(x) for x in f.readline()[:-1].split(' ')]
    G = [int(x) for x in f.readline()[:-1].split(' ')]
    if P == 2:
        i = sum(x%2 == 0 for x in G)
        j = N - i
        result = i + j/2 + j%2
    elif P == 3:
        i = sum(x%3 == 0 for x in G)
        j = sum(x%3 == 1 for x in G)
        k = N - i - j
        result = i + min(j,k) + int(math.ceil(1.0*abs(j-k)/3))
    else:
        i = sum(x%4 == 0 for x in G)
        j = sum(x%4 == 1 for x in G)
        k = sum(x%4 == 2 for x in G)
        l = N - i - j - k
        if k % 2 == 0:
            result = i + k/2 + min(j,l) + int(math.ceil(1.0*abs(j-l)/4))
        else:
            result = i + k/2 + 1 + min(j,l) + (abs(j-l) >= 3) * int(math.ceil(1.0*(abs(j-l)-2)/4))
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()