import copy
import itertools

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
  #n = int(raw_input())  
  des,hor = [(int(s)) for s in raw_input().split(' ')]
  hor_pos = []
  max_time = 0
  for h in range(hor):
    hor_pos.append([int(s) for s in raw_input().split(" ")])
  for hi in hor_pos:
    arr_time = (float(des) - hi[0]) / hi[1]
    if (arr_time > max_time):
      max_time = arr_time
  res_str = "%.6f" %(float(des) / max_time)
  case_str = "Case #%d: " %case
  print case_str + res_str
  #print case_str + "%d,%d" %(max_circle,max_pair_circle)
