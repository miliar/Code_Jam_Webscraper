__author__ = 'kozya'
import math
f = open("ind.txt","r")
out = open("outd.txt","w")
cases = int(f.readline())
for case in xrange(1,cases+1):
    n = int(f.readline())
    mas = [int(x)-1 for x in list(f.readline().split())]
    hits = 0
    for i in xrange(n):
        if i!=mas[i]:hits+=1
    out.write("Case #%d: %.6f\n" % (case,hits))
  