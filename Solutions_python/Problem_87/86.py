#! /usr/bin/python

import sys
from math import sqrt
from decimal import *
getcontext().prec = 100

def solve(x, s, r, t, nb_walkways, walkways):

  walkways.append([x, x, 1])

#  print x, s, r, t
#  print walkways

  rest_run_time = t

  cur_pos = 0.0
  cur_time = 0.0
  for w in walkways:
#    print cur_pos, cur_time, x, w[0], rest_run_time

    diff_pos = (w[0] - cur_pos)
    if rest_run_time <= 0:
      cur_time += diff_pos / s

    else:
      time_if_run = diff_pos / r
      if time_if_run < rest_run_time:
        cur_time += time_if_run
        rest_run_time -= time_if_run
      else:
        point_stop_run = cur_pos + r * rest_run_time
        cur_time += rest_run_time
        cur_time += (w[0] - point_stop_run) / s
        rest_run_time = 0
      
    cur_pos = w[1]

    if w[1] <= x:
      cur_time += (w[1] - w[0]) / (s + w[2])
      
  # add running time
  # on slowest walkways firstly
  if rest_run_time > 0:
#    print "a"
    slowest_walkways = sorted(walkways, key=lambda x: x[2])
    for w in slowest_walkways:
#      print "a", cur_time, rest_run_time, w
      if rest_run_time <= 0:
        break
      else:
        diff_pos = w[1] - w[0]
        cur_time -= diff_pos / (s + w[2])
#        print cur_time

        time_if_run = diff_pos / (r + w[2])
#        print "b", diff_pos, time_if_run
        if time_if_run < rest_run_time:
          cur_time += time_if_run
          rest_run_time -= time_if_run
        else:
          point_stop_run = w[0] + (r + w[2]) * rest_run_time
          cur_time += rest_run_time
          cur_time += (w[1] - point_stop_run) / (s + w[2])
          rest_run_time = 0
          break

#  print rest_run_time

  return cur_time
      
fd = open(sys.argv[1])
num_cases = int(fd.readline())

for i in range(0, num_cases):
  (x, s, r, t, nb_walkways) = [int(item) for item in fd.readline().split(" ")]

  walkways = []
  for j in xrange(nb_walkways):
    (b, e, w) = [float(item) for item in fd.readline().split(" ")]
    walkways.append((b, e, w))

  print "Case #%d: %.10f" % (i+1, solve(x, s, r, t, nb_walkways, walkways))

