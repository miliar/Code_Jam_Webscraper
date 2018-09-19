from itertools import *
from operator import *
fp = open('C-large.in')

for t in range(int(fp.readline())):
    N = int(fp.readline())
    C = map(int, fp.readline().split())
    print "Case #%d:"%(t+1), ("NO",sum(C)-min(C))[reduce(xor,C) == 0]
