import sys, re

def xor(A,B):
  return (A & 0xFFFFFFFF) ^ B
  
N = sys.stdin.readline()

for case in range(0,int(N)):
  M = int(sys.stdin.readline())
  seq = [int(x) for x in sys.stdin.readline().split()]

  res = -1
  for i in range(1,1<<M-1):
    act = i
    sums_B = [0,0]
    sums_D = [0,0]
    for s in seq:
      ind = act%2
      sums_B[ind] = xor(sums_B[ind], s)
      sums_D[ind] += s
      act/=2
    if sums_B[0]==sums_B[1]: res=max(res, sums_D[0], sums_D[1])
      
  if res<0: print "Case #%d: NO" % (case+1)
  else: print "Case #%d: %d" % (case+1,res)

