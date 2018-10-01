def ints():
  return [int(x.strip()) for x in raw_input().split(' ')]
cases = input()

import numpy as np
for casenum in range(1, cases+1):
  n = input()
  nums = ints()
  nums = sorted(zip(nums, range(n)))
  B = [[0]*(n-1) for _ in range(n)]
  for i in range(n):
    for j in range(i):
      B[i][j] = 0 if nums[i][1] > nums[j][1] else 1
  C0 = [sum(B[i][j] ^ 0 for i in range(n) if i > j) for j in range(n-1)]
  C1 = [sum(B[i][j] ^ 1 for i in range(n) if i > j) for j in range(n-1)]
  C = [min(C0[i], C1[i]) for i in range(len(C0))]
  s = sum(C)
  print "Case #" + str(casenum) + ":", s