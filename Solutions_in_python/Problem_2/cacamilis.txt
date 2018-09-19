#!/usr/bin/python
import sys
import time
import os
import pdb

import datetime
#x = open('B-small-attempt1.in', 'r')
x = open('B-small-attempt4.in', 'r')
#x = open('IN.in', 'r')
y = open('OUT.txt', 'w')
cases = x.readline().strip()

txt = r''
for i in range(1,int(cases)+1):
  tu = int(x.readline().strip())
  if tu > 59:
    h = tu/60
    m = tu%60
  else:
    h = 0 
    m = tu
  t = datetime.time(h,m)
  na, nb = x.readline().strip().split(' ')
  aNTG = [] #need to go
  aRTG = [] #ready to go
  bNTG = []
  bRTG = []
  for a in range (0, int(na)):
    aD, aA = x.readline().strip().split(' ')
    #datetime.time(int(aD.split(':')[0]), int(aD.split(':')[1]))
    c = 0
    if int(aA.split(':')[1])+m > 59: c = 1
    aNTG.append(datetime.time(int(aD.split(':')[0]), int(aD.split(':')[1])))
    bRTG.append(datetime.time((int(aA.split(':')[0])+h+c)%24, (int(aA.split(':')[1])+m)%60))
  for b in range (0, int(nb)):
    bD, bA = x.readline().strip().split(' ')
    c = 0
    if int(bA.split(':')[1])+m > 59: c = 1
    bNTG.append(datetime.time(int(bD.split(':')[0]), int(bD.split(':')[1])))
    aRTG.append(datetime.time((int(bA.split(':')[0])+h+c)%24, (int(bA.split(':')[1])+m)%60))
  aNTG.sort()
  aRTG.sort()
  bNTG.sort()
  bRTG.sort()
  aRTG.reverse()
  bRTG.reverse()
  print 'an = ', aNTG, ' \nar = ', aRTG
  print 'bn = ', bNTG, ' \nbr = ', bRTG
  aT = 0
  bT = 0 #b trains
  if na == '0':  bT = int(nb)
  else:  
    for tb in bNTG:
      if len(bRTG) !=0:
        if bRTG[-1] > tb:  bT = bT + 1
        else:  bRTG.pop()
      else:  bT = bT + 1
  if nb == '0':  aT = int(na)
  else:
    for ta in aNTG:
      if len(aRTG)!=0:
        if aRTG[-1] > ta:  aT = aT + 1
        else:  aRTG.pop()
      else:  aT = aT + 1
  print r'Case #' + str(i) + ': '+ str(aT) +' ' + str(bT)
  y.writelines('Case #' + str(i) + ': '+ str(aT) +' ' + str(bT))
  y.write('\n')

x.close()
y.close()


"""
na = len(an)
nb = len(bn)
aT = 0
bT = 0 #b trains

print len(an), len(ar)
print len(bn), len(br)

if na == '0':  
  bT = int(nb)
else:  
  for tb in bn:
    print bn.index(tb)
    if br:
      if br[-1] > tb:  
        bT = bT + 1
        print 'added 1', br[-1], tb
      else:  print br.pop(), tb
    else:  
      print 'added 1', br[-1], tb
      bT = bT + 1

if nb == '0':  
  aT = int(na)
else:
  for ta in an:
    print an.index(ta)
    if ar:
      if ar[-1] > ta:
        aT = aT + 1
        print 'added 1'
      else:  print ar.pop()
    else:
      print 'added 1'
      aT = aT + 1

print r': '+ str(aT) +' ' + str(bT)
"""
