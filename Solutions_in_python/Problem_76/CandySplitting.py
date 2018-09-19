import sys
import string
import math
      
def cry(lst):
    for i in xrange(20):
        count = 0
        for j in xrange(len(lst)):
            if lst[j][i] == '1':
                count += 1
        if count % 2 != 0:
            return True
    return False


def binary(n):
    rep = bin(n)[2:]
    return ('0' * (20 - len(rep))) + rep
    

f = open('C-large.in.txt','rU')
T = int(f.readline().strip())

for i in xrange(1,T+1):
    N = int(f.readline().strip())
    candy = f.readline().strip().split()
    candyInt = []
    candyBin = []
    for j in candy:
        candyInt.append(int(j))
        candyBin.append(binary(int(j)))
    if cry(candyBin):
        print "Case #%d: NO" %i
    else:
        result = 0
        for n in candyInt:
            result += n
        result = result - min(candyInt)
        print "Case #%d: %d" % (i, result)
