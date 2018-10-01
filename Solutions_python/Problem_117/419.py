#!/usr/bin/python3
import sys
import math
import fractions
from array import array
from operator import itemgetter

def rl(convert=''):
  line = sys.stdin.readline().split()
  for i,c in enumerate(convert):
    if c=='i':
      line[i]=int(line[i])
    elif c=='s':
      pass
    elif c=='f':
      line[i]=float(line[i])
  # if len(line)==1:
  #   return line[0]
  return line

def gcd(*args):  
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g = fractions.gcd(g,args[i])    
  return g

def lcm(*args):
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g *= args[i]  
  return g/gcd(*args)


#--------------------------------------------------------------------#

t = rl('i')[0]

for index in range(1,t+1):
  n,m = rl('ii')
  lawn = list()
  for i in range(n):
    lawn.append(rl('i'*m))

  possible = 'YES'

  for i in range(n):
    for j in range(m):
      # print(lawn[i][j],max(lawn[i]),max(map(itemgetter(j),lawn)))

      if lawn[i][j] != max(lawn[i]) and lawn[i][j]!=max(map(itemgetter(j),lawn)):
        possible = 'NO'
        break
    if possible=='NO':
      break

  print('Case #%(i)d: %(a)s' % {'i':index, 'a':possible})