#import psyco
T = int(raw_input())

for case in xrange(1, T+1):
  P = int(raw_input())
  num = 2**P
  M = map(int, raw_input().split())
  prices = []
  for i in xrange(P):
    prices.append(map(int,raw_input().split()))
  

  temp = []
  for i in xrange(0,num,2):
    temp.append(min(M[i], M[i+1]))

  ans = 0
  for i in xrange(P):
    for t in temp:
      if t == 0:
        ans += 1
    for j in xrange(len(temp)):
      temp[j] -= 1
    ttemp = []
    if len(temp) > 1:
      for j in xrange(0, len(temp), 2):
        ttemp.append(max(0, min(temp[j], temp[j+1])))
    temp = ttemp

  print "Case #%d: %d" %(case, ans)

