import sys

def getint():
  return int(sys.stdin.readline())

def getints():
  return [int(s) for s in sys.stdin.readline().split()]

def getline():
  return sys.stdin.readline().rstrip()

def solve(N, K, B, T, Xs, Vs):
    arrived = 0
    swaps = 0
    to_swap = 0
    for x, v in reversed(zip(Xs, Vs)):
        if arrived >= K:
            break
        if v >= float(B - x) / T:
            arrived +=1
            swaps += to_swap
        else:
            to_swap += 1

    if arrived >= K:
        return swaps
    return 'IMPOSSIBLE'

C = getint()
for i in range(C):
  N, K, B, T = getints()
  Xs = getints()
  assert len(Xs) == N
  Vs = getints()
  assert len(Vs) == N

  print 'Case #%d: %s' % (i+1, solve(N, K, B, T, Xs, Vs))
