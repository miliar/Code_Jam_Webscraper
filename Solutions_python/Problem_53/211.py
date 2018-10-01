T = int(raw_input())
N = []
K = []
for i in range(T):
  n, k = [int(s) for s in raw_input().split()]
  N.append(n)
  K.append(k)
M = max(N)
A = [0]
for i in range(M + 1):
  A.append(A[i] * 2 + 1)
for i in range(T):
  if K[i] % (A[N[i]] + 1) == A[N[i]]:
    s = 'ON'
  else:
    s = 'OFF'
  print 'Case #{0}: {1}'.format(i + 1, s)
