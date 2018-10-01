# -*- coding: utf-8 -*-
"""
Created on Sat May 02 12:29:40 2015

@author: petrs
"""

maxnum = 10**6

def obrat(k):
    tmp = str(k)
    tmp2 = tmp[::-1]
    l = int(tmp2)
    return l

initial = list([0] * (maxnum + 1))
initial[1] = 1
seted = 1
toexpand = set([1])

while seted < maxnum:
    assert len(toexpand)>0
    newexpand = set([])    
    
    for i in toexpand:
        if i<maxnum and initial[i+1]==0:
            initial[i+1] = initial[i] + 1
            newexpand.add(i+1)
            seted += 1
        j = obrat(i)
        if j<=maxnum and initial[j]==0:
            initial[j] = initial[i] + 1
            newexpand.add(j)
            seted += 1
        
    toexpand = newexpand    

f = open('C:\Users\petrs\Downloads\A-small-attempt02.in', 'r')
g = open('C:\Users\petrs\Downloads\output21.txt', 'w')

T = int(f.readline().split()[0])

for i in xrange(T):
  M = int(f.readline().split()[0])
  g.write("Case #%i: %i\n" % (i+1,initial[M]) )   
    
f.close()
g.close()