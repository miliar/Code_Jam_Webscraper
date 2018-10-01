#!/usr/bin/python -tt

import sys

def calculate():
  filename='A-large.in'
  f=open(filename,'rU')
  lines=[]
  count=[]
  lines=f.read().split('\n')
  #print lines[0]
  #print lines[1].split(' ')
  for j in range(int(lines[0])):
   n,m=lines[j+1].split(' ')
   #print '\n'+n,m
   m=int(m)
   if n==m*'-':
     print 'Case #{}: 1'.format(j+1)
   elif n==len(n)*'+':
     print 'Case #{}: 0'.format(j+1)

   else:
     n=list(n)
     count=0
     for i in range(len(n)-m+1):
          while n[i]=='-' :
            for k in range(m):
                if n[k+i]=='-':
                  n=n[:k+i]+list('+')+n[k+i+1:]
                elif n[k+i]=='+':
                  n=n[:k+i]+list('-')+n[k+i+1:]
            count+=1
            if n[i]=='-':
              break

       #print 'Case #{}: {}'.format(j+1,count)
     mount=0
     for next in n:
       if next=='-':
         mount=1
         break

     if mount==1:
       print 'Case #{}: {}'.format(j+1,'IMPOSSIBLE')
     elif mount==0:
       print 'Case #{}: {}'.format(j+1,count)
   #print n, len(n), count


if __name__ == '__main__' :
   sys.stdout = open('smallinput1.out', 'a')
   calculate()
