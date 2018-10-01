T = int(raw_input())

for caseNum in range(1, T+1):
  C, F, X = [float(a) for a in raw_input().split(' ')]

  v = 2.
  prevTime = X / v

  while True:
    time = (prevTime - X / v) + C / v
    v += F
    time += X / v
    if time < prevTime:
      prevTime = time 
    else:
      print "Case #{0}: {1}".format(caseNum, prevTime)
      break
