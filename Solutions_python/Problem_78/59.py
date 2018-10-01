
import os
import fileinput
import math
import pdb
import re
import getopt,sys
import copy



def readMat(filename) :
  result = []
  mfile = fileinput.input(filename)
  for line in mfile :
    ar = line.split()
    if len(ar)>0 :
      row = []
      for item in ar :
        value = float(item)
        row.append(value)
      result.append(row)
  return result

def trimString(s) :
    l = len(s)
    assert l>0
    outs=[]
    curc=''
#    pdb.set_trace()
    for i in range(0,l):
        c = s[i]
        if c == 'A' or c == 'B' or c == 'C':
            if not c==curc:
                curc=c
                outs.append(c)

    return outs


def gcd(a, b):
    if int(a)==1 or int(b)==1:
        return int(1)
    else:
        if a>b:
            c=a
            a=b
            b=c
        b=b%a
        if b==0:
            return a
        else:
            return gcd(b, a)



if len(sys.argv)<2:
  print('usage: 01.py input output')
  sys.exit()

fname = sys.argv[1]
if len(sys.argv)<3:
    ofname='output.txt'
else:
    ofname = sys.argv[2]

fin = fileinput.input(fname)
of = open(ofname,'w')

line=fin[0]

ntc=int(line)

assert ntc>0

print(ntc)

for i in range(0, ntc):
    line = fin[i+1]
    print(line)

    ar=line.split()

    assert len(ar)>2

    N=int(ar[0])
    pd=int(ar[1])
    pg=int(ar[2])

    flag=True

    if pg==100 and pd<100:
        flag=False
    elif pd>0 and pg==0:
        flag=False
    elif pd==0 and pg==0:
        flag=True
    else:
        dv=gcd(pd, 100)
        print(str(pd)+':'+str(dv))
        mul=int(100/dv)
        print(mul)

        if mul<=N:
            flag=True
        else:
            flag=False

    if flag:
        line='Case #'+str(i+1)+': Possible\n'
    else:
        line='Case #'+str(i+1)+': Broken\n'


    of.write(line)


#fin = fileinput.input(fname)
#of = open(ofilename,'w')
