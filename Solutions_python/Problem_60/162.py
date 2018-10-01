import sys

input = open(sys.argv[1])
n = int(input.readline())

for nCase in xrange(1, n+1):
  N,K,B,T = map(lambda a: int(a), input.readline().strip().split(' ') )
  #print 'K', K, 'B', B
  x = map(lambda a: int(a), input.readline().strip().split(' ') )
  v = map(lambda a: int(a), input.readline().strip().split(' ') )

  arrived = 0
  for i in xrange(N):
    x[i] += v[i] * T

    if x[i] >= B:
      arrived += 1

  res = ''
  a = 0
  if arrived < K:
    res =  'IMPOSSIBLE'
  else:
    #print x
    swap = 0
    for i in xrange(N-1, -1, -1):
      if x[i] >= B:
        for j in xrange(i+1, N):
          if x[i] > x[j] and x[j] < B:
            swap += 1

        a += 1

        if a >= K:
          break

    res = str(swap)

  print 'Case #%d: %s'%(nCase, res)
