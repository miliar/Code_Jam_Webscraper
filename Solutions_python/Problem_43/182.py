#!/usr/bin/python
'''
Solution for Google Code Jam
Created on 2009-9-13
@author: Qihe Bian
'''
import sys
import re
from collections import *

class Buffer:
    buffer=''
    def write(self, s):
        Buffer.buffer += s
    def __str__(self):
        return Buffer.buffer
    def __repr__(self):
        return Buffer.buffer
        
def main():
    global d
    for case in range(input()):
        d.clear()
        s=raw_input();
        k=0
        l=len(s)
        for i in range(l):
            if i==0:
                d[s[i]]=1
                k=1
                continue
            if d.has_key(s[i]):
                continue
            if k==1:
                d[s[i]]=0
                k+=1
            else:
                d[s[i]]=k
                k+=1
        base=k
        if k==1:
            base=2
        sum=0
        r=1
        for i in range(l):
            sum+=d.get(s[l-i-1])*r
            r*=base
        print 'Case #%d: %d' % (case + 1, sum)
            
filename=''
filename=raw_input() #only the filename body without ext
filein=filename+'.in'
fileout=filename+'.out'
_stdout=sys.stdout
sys.stdin=open(filein,'r')
sys.stdout=open(fileout,'w')
#sys.stdout=Buffer()

d=defaultdict(int)
main()
sys.stdout=_stdout
print Buffer()
