#!/usr/bin/python
try:
  import psyco
  psyco.full()
except ImportError:
  print >> sys.stderr, "No Psyco available ! To run faster, please, please install it!\n"



import sys
import math

def count(x):
    d = [0]*10
    for i in xrange(len(x)):
        d[ord(x[i])-ord('0')] = d[ord(x[i])-ord('0')] + 1
    return d

def next_item(x, d):
#    print "calculating next_item ", x, d 
    i = ord(x) - ord('0')+1
    while i < 10:
        if d[i] != 0:
            return chr(i+ord('0'))
        i = i+1
    return ""

def first_sequence(d):
    x = ""
    for i in xrange(10):
        for j in xrange(d[i]):
            x = x + chr(i + ord('0'))
    return x

def next(x, d):
#    print "calculating next for ", x
    if x == "":
        return ""
    d1 = d*1
    d1[ord(x[0]) - ord('0')] = d1[ord(x[0]) - ord('0')] - 1
    f = next(x[1:], d1)
    if f != "":
        return x[0]+f
    else:
        ni = next_item(x[0], d)
        if (ni != ""):
            d1 = d *1
            d1[ord(ni) - ord('0')] = d1[ord(ni) - ord('0')] - 1
            return ni + first_sequence(d1)
        else:
            return ""
        
    return ""

def first_item(d):
    for i in xrange(len(d)):
        if i == 0: continue
        if d[i] != 0: return chr(i+ord('0'))
    return ""

def solve(x):
    d = count(x)
    n = next(x, d)
    if n != "":
        return n
    f = first_item(d)
    if f != "":
        d[ord(f) - ord('0')] =  d[ord(f) - ord('0')] - 1
        return f + '0' + first_sequence(d)
    return ""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Usage: %s file' % sys.argv[0])
        sys.exit(1)

    f = open(sys.argv[1])
    NTEST =  int(f.readline())
    for i in xrange(NTEST):
        x = f.readline()
        #print x
        print ('Case #%d:' % (i + 1)),
        print solve(x.strip())

