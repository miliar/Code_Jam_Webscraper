#!/usr/bin/env python

import os 
import sys

fd_in = open(sys.argv[1], 'r')
name_out = sys.argv[1].split('.in')[0] + '.out' 
fd_out = open(name_out, 'w')

data = fd_in.read().split('\n')

if len(data) == 1:
   print 'file empty'
   sys.exit()

T = int(data[0])
if T > 100 or T < 1:
   print 'ERROR in T'
   sys.exit()

if len(data) < T+1:
   print 'No enough data'
   sys.exit()

cases = 1
i = 1
while cases <= T:
   
   C = float(data[i].split()[0])
   if C < 1 or C > 500 and sys.argv[2] == 'short':
      print 'Error in C'
      sys.exit()
   if C < 1 or C > 10000 and sys.argv[2] == 'large':
      print 'Error in C'
      sys.exit()
   F = float(data[i].split()[1])
   if F < 1 or F > 4   and sys.argv[2] == 'short':
      print 'Error in F'
      sys.exit()
   if F < 1 or F > 100   and sys.argv[2] == 'large':
      print 'Error in F'
      sys.exit()
   X = float(data[i].split()[2])
   if X < 1 or X > 2000 and sys.argv[2] == 'short':
      print 'Error in X'
      sys.exit()
   if C < 1 or C > 100000 and sys.argv[2] == 'large':
      print 'Error in X'
      sys.exit()
   
   t_buy = {}
   t_goal = {}
   t_total = {}
   t_buy[0] = (C /2) 
   t_goal[0] =(X/2)
   t_total[0] = t_goal[0]
   j = 1
   while 1:
      t_buy[j] = (C / (F*j+2)) 
      t_goal[j] =(X/(F*j+2))
      t_total[j] = sum(t_buy.values())-t_buy[j]+ t_goal[j]
      if t_total[j] > t_total[j-1]:
           print 'Case #' + str(i) + ': ' + str(t_total[j-1])
           fd_out.write('Case #' + str(i) + ': ' + str(t_total[j-1]) + '\n')
           break
      j = j + 1

   cases = cases + 1
   i = i + 1

fd_in.close()
fd_out.close()