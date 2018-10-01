#!/usr/bin/python3
import sys

def line():
  return sys.stdin.readline().strip()

table = [] 
def time(farms, farm_cost, farm_rate, goal):
  time = 0

  if farms > 0:
    time = table[farms-1] + farm_cost / (2 + farm_rate * (farms - 1))
  table[farms] = time
  time = time + goal / (2 + farms * farm_rate)

  return time

cases = int(line())
for i in range(cases):
  C, F, X = [float(x) for x in line().split(" ")]
  table = {}

  farms = 0
  oldtime = float("inf")
  nexttime = time(farms, C, F, X)
  while nexttime < oldtime:
    farms += 1
    oldtime = nexttime
    nexttime = time(farms, C, F, X)

  print("Case #{}: {}".format(i+1, round(oldtime, 7)))
