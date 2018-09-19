import sys

def solve(N,shrooms):
  # Method A
  eatenA = 0
  for i in range(1,N):
    if shrooms[i] < shrooms[i-1]: eatenA += shrooms[i-1]-shrooms[i]
  # Method B
  maxdif = 0
  for i in range(1,N):
    dif = shrooms[i-1]-shrooms[i]
    if dif > maxdif: maxdif = dif
  eatenB = 0
  for i in range(1,N):
    if shrooms[i-1] >= maxdif: eatenB += maxdif
    else: eatenB += shrooms[i-1]
  return eatenA, eatenB

f = open(sys.argv[1],"r")
T = int(f.readline())
for case in range(1,T+1):
  N = int(f.readline())
  shrooms = map(int, f.readline().strip().split())
  A, B = solve(N,shrooms)
  print "Case #%i: %i %i" % (case, A, B)

