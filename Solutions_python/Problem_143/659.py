
T = int(raw_input())

for caseNum in range(T):
  [A, B, K] = [int(a) for a in raw_input().split(' ')]



  count = 0
  for a in range(A):
    for b in range(B):
      if a & b < K:
        count += 1

  print "Case #{0}: {1}".format(caseNum + 1, count)