#! /usr/bin/env python
import sys

testcases = int(sys.stdin.readline())
case = 1
while case <= testcases:
  line = sys.stdin.readline()
  C, F, X = (float(x) for x in line.split())
  rate = 2
  best_time = 0

  while True:
    # time it takes to get C with current rate
    time_to_c = C / rate
    get_x_wo_buying = X / rate
    get_x_with_buying = (X / (rate + F)) + time_to_c
    if get_x_with_buying < get_x_wo_buying:
      best_time += time_to_c
      rate += F
    else:
      best_time += get_x_wo_buying
      break

  print "Case #%d: %0.7f" % (case, best_time) 
  case += 1
