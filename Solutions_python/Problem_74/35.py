#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  fields = fh.readline().strip().split()
  buttons = fields[1:]
  i_pushes = int(fields[0])
  pushes = []
  for i in range(i_pushes):
    pushes += [buttons[2*i]+buttons[2*i+1]]
    #print pushes
  cases += [pushes]

#print cases

try:
  line = fh.readline().strip()
  if line == "":
    print "good read"
except:
  print "good read"

fh.close()


fh = open("out.txt","w")
for (i,case) in enumerate(cases):
  b_goals = map(lambda y: int(y[1:]) , filter(lambda x: "B" in x, case))
  o_goals = map(lambda y: int(y[1:]) , filter(lambda x: "O" in x, case))
  #print b_goals  
  #print o_goals
  i_move = 0
  b_pos = 1
  o_pos = 1
  while len(b_goals + o_goals) >0:
    i_move += 1
    bp = 0
    if len(b_goals)>0:
      if b_goals[0]==b_pos:
        if case[0] == "B"+str(b_pos):
          b_goals = b_goals[1:]
          case = case[1:]
          bp = 1
      else:
        if b_goals[0]<b_pos:
          b_pos += -1
        elif b_goals[0]>b_pos:
          b_pos += 1
        else: 
          print "b issue"
    if len(o_goals)>0:
      if o_goals[0]==o_pos:
        if case[0] == "O"+str(o_pos) and bp == 0:
          o_goals = o_goals[1:]
          case = case[1:]
      else:
        if o_goals[0]<o_pos:
          o_pos += -1
        elif o_goals[0]>o_pos:
          o_pos += 1
        else: 
          print "o issue"
  print >> fh, "Case #"+str(i+1)+": "+str(i_move)

fh.close()

