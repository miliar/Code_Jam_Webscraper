import sys

inputFile = sys.stdin
count = int(inputFile.readline())

for lineno in xrange(1, count+1):
  N, K, B, T = map(int, inputFile.readline().split())
  X = map(int, inputFile.readline().split())
  V = map(int, inputFile.readline().split())
  
  for i in xrange(N-1):
    if X[i] == X[i+1] and V[i] > V[i+1]:
      t = V[i]
      V[i] = V[i+1]
      V[i+1] = t

  times = []
  for i in xrange(N):
    times.append(1.0* (B - X[i]) / V[i])

  together = [1]*N

  swaps = 0
  chicks = 0

  """
  for i in xrange(N):
    if times[i] > T: 
      #never get there
      continue

    for j in xrange(i+1, N):
      if times[i] < times[j] and times[j] > T:
        swaps += together[i]
      else:
        together[j] += together[i]
        break
        
    chicks += 1
  """
  bad = 0
  for i in xrange(N-1, -1, -1):
    if chicks >= K:
      break

    if times[i] <= T: 
      swaps += bad
      chicks += 1
      continue
    else:
      bad += 1

  if chicks < K:
    swaps = "IMPOSSIBLE"

  print "Case #%d:" % lineno, 
  print swaps
  sys.stdout.flush()

  lineno += 1
