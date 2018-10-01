#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]
f = open(filename, 'r+')

case = int(f.readline())
for c_num in range(0, case):
  line = f.readline().strip().split()
  (C, D) = int(line[0]), int(line[1])

  data = []
  for c in range(C):
    PV = f.readline().strip().split()
    P = int(PV[0])
    V = int(PV[1])
    data.append((P, V))
  data.sort(cmp=lambda x,y: cmp(x[0], y[0]))

  ans = 0.0
  for left in range(len(data)):
    for right in range(left, len(data)):
      vendor_count = 0
      for n in range(left, right + 1):
        vendor_count += data[n][1]
      cur_distance = data[right][0] - data[left][0]
      need_distance = D * (vendor_count - 1)
      # print left, right, vendor_count, need_distance      
      tmp = (need_distance - cur_distance) / 2.0
      if ans < tmp:
        ans = tmp
      
  print "Case #%d: %s" % (c_num+1, ans)
