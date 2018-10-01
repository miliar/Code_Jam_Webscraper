import numpy as np
import sys
import re
import math
e=open('C:\Users\haki!\Desktop\entrer4.txt','r')
s=open('C:\Users\haki!\Desktop\sorter4.txt','w')

N=int(e.readline())#number of case
for i in range(1,N+1):
    X=map(int,e.readline().split())
    X,R,C=X[0],X[1],X[2]
    if (R%X!=0) and (C%X!=0):
       CC='RICHARD'
    elif (R%X==0) and (C%X==0):
       CC='GABRIEL'
    else :
         if X==1:CC='GABRIEL'
         elif X==2:CC='GABRIEL'
         elif X==3:
              if R==1 or C==1:CC='RICHARD'
              else:CC='GABRIEL'
         elif X==4:
              if R==2 or C==2:CC='RICHARD'
              elif R==1 or C==1:CC='RICHARD'
              else:CC='GABRIEL'

    s.write('Case #%d: %s\n' %(i,CC))
    print X,R,C
    print 'Case #%i: %s\n' % (i,CC)

e.close()
s.close()