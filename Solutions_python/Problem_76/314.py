import sys
import operator

f = open('clarge.in','r')
t = int(f.readline().strip())

for z in xrange(t):
    n = int(f.readline().strip())
    ln = map(int, f.readline().strip().split())
    x = 0
    for i in ln: x = operator.xor(x,i)
    if x==0: t = sum(ln) - min(ln)
    else: t='NO'
    print 'Case #'+str(z+1)+': '+str(t)
