from collections import deque
from collections import defaultdict

tc = int(raw_input())  # read a line with a single integer

for ii in xrange(1, tc + 1):
  D, N = [int(s) for s in raw_input().split(" ")]  # read a list of integers
  K = [0 for i in range(N)]
  S = [0 for i in range(N)]  
  for jj in range(N):
    K[jj], S[jj] = [int(s) for s in raw_input().split(" ")]  # read a list of integers

  mx = -1
  for i in range(N):
    if mx == -1:
      mx = float(D-K[i])/float(S[i])
    else:
      mx = max(mx, float(D-K[i])/float(S[i]))
    
  print "Case #{0}: {1:.6f}".format(ii, float(D)/float(mx))

