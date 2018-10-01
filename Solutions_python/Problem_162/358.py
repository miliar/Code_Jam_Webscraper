import os
import math
import copy
import sys
from collections import *

#def count(k):
#    if k==1:
#        rec[k] = 1
#        return(1)
#    elif rec[k]>0:
#        return(rec[k])
#    else:
#        print(k)
#        c = str(k)
#        l = len(c)
#        c1 = ''.join([c[l-i-1] for i in range(l)])
#        flag = True
#        if c1[0] == '0':
#            flag = False
#        rev = int(c1)
#        a = count(k-1)
#        if rev<k and flag:
#            #print(rev)
#            b = count(rev)
#            rec[k] = min(a,b)+1
#            return(min(a,b)+1)
#        else:
#            rec[k] = a+1
#            return(a+1)

os.chdir('/Users/Dana/Documents/0502')
f = open('A-small-attempt0.in','r')
fo = open('A.out','w')
T = int(f.readline())
n = [0]*T

for ite in range(T):
    n[ite] = int(f.readline())
rec = [0]*(max(n)+1)
rec[1] = 1
for i in range(2,max(n)+1):
    c = str(i)
    l = len(c)
    c1 = ''.join([c[l-i-1] for i in range(l)])
    rev = int(c1)
    if rev<i and c1[0]!='0':
        rec[i] = min(rec[rev],rec[i-1])+1
    else:
        rec[i] = rec[i-1]+1
for ite in range(T):
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    fo.write(str(rec[n[ite]]))
    fo.write('\n')
fo.close()

