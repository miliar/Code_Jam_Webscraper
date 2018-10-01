from sys import *

def solve(ar1, ar2):
  ar3 = [val for val in ar1 if val in ar2]
  if len(ar3) == 1:
    return str(ar3[0])
  elif len(ar3) > 1:
    return 'Bad magician!'
  elif len(ar3) == 0:
    return 'Volunteer cheated!'

cases = int(raw_input())
for _ in xrange(cases):
  ans1 = int(raw_input())
  fr1 = []
  for r1 in xrange(4):
    fr1.append(map(int,stdin.readline().split()))
  ans2 = int(raw_input())
  fr2 = []
  for r2 in xrange(4):
    fr2.append(map(int,stdin.readline().split()))
  res = solve(fr1[ans1-1], fr2[ans2-1])

  print "Case #%d:" %(_+1), res
