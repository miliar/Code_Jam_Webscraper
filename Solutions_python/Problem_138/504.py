#!/usr/bin/python3
import sys

def line():
  return sys.stdin.readline().strip()

def dwar(naomi, ken):
  score = 0
  
  while len(naomi) > 0:
    if naomi[0] > ken[0]:
      naomi.pop(0)
      ken.pop(0)
      score +=1
    else:
      naomi.pop(0)
      ken.pop()

  return score

def war(naomi, ken):
  score = 0
  naomi.reverse()
  ken.reverse()
  for i in range(len(naomi)):
    if naomi[i] > ken[0]:
      ken.pop()
      score += 1
    else:
      ken.pop(0)

  return score

cases = int(line())
for i in range(cases):
  line() # blocks
  naomi = [float(x) for x in line().split(" ")]
  ken = [float(x) for x in line().split(" ")]
  war_score = war(sorted(naomi), sorted(ken))
  dwar_score = dwar(sorted(naomi), sorted(ken))
  print("Case #{}: {} {}".format(i+1, dwar_score, war_score))
