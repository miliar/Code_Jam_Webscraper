tc = int(raw_input())
T = tc
while tc > 0:
  tc -= 1
  [size, arr] = raw_input().split(' ')
  arr = map(int, list(arr))
  res = 0
  for i in xrange(int(size)+1):
    if res < i:
      res = i
    res += arr[i]
  print "Case #{}: {}".format(T-tc, res-sum(arr)) 
