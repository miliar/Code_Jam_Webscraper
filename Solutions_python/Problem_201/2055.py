t = int(raw_input())  # read a line with a single integer
for ii in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

  filled = [0 for i in range(n+2)]
  filled[0] = 1
  filled[n+1] = 1
  rLst = [0 for i in range(n+2)]
  lLst = [0 for i in range(n+2)]
  
  for q in range(k):
    cur = 0
    for i in range(1,n+1):
      if filled[i]==1:
        cur = 0
        continue
      else:
        lLst[i] = cur
        cur += 1

    cur = 0
    for i in range(n,0,-1):
      if filled[i]==1:
        cur = 0
        continue
      else:
        rLst[i] = cur
        cur += 1

    curMx = -1
    curMn = -1

    curS = -1
    for i in range(1,n+1):
      if filled[i] == 0:
        mn = min(rLst[i],lLst[i])
        mx = max(rLst[i],lLst[i])
        if mn > curMn:
          curMn = mn
          curMx = mx
          curS = i
        elif mn == curMn and mx > curMx:
          curMx = mx
          curS = i
    filled[curS] = 1
  
  print "Case #{}: {} {}".format(ii, curMx, curMn)
  # check out .format's specification for more formatting options
