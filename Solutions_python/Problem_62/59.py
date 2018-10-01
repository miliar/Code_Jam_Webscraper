import sys
import re
from pprint import pprint

input = sys.stdin
T=int(input.readline())
for i in xrange(1,T+1):
    N=int(input.readline())
    Ps = []
    for ii in xrange(1, N+1):
        Ps.append([int(x) for x in input.readline().split()])
    c = 0
    for a in xrange(len(Ps)):
        for b in xrange(a+1, len(Ps)):
            aa = Ps[a]
            bb = Ps[b]
            if (aa[0] < bb[0] and aa[1] > bb[1]) or (aa[1] < bb[1] and aa[0] > bb[0]):
                c+=1
    print "Case #%s: %s" % (i,c)
               
