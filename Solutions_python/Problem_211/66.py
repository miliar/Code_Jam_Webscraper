eps = 1e-7
step = 1e-2

def DP(a):
  n = len(a)
  dp = [0] * (n+1)
  dp[0] = 1
  #print(dp)
  for p in a:
    tmp = [0] * (n+1)
    for i in range(n):
      tmp[i] += dp[i] * (1-p)
      tmp[i+1] += dp[i] * p
    dp = tmp
    #print(dp)
  return dp

def ans(k, a):
  dp = DP(a)
  return sum(dp[i] for i in range(k, len(a)+1))

def ceff(k, a):
  dp = DP(a)
  return dp[k-1]

def solve():
  n, k = input().split()
  n, k = int(n), int(k)
  u = float(input())
  a = list(map(float, input().split()))
  #print(k, a)
  #return ans(k, a)

  while u > eps:
    mx, mxi = 0, -1
    for i in range(len(a)):
      if a[i] > 1 - eps: continue
      c = ceff(k, a[:i] + a[i+1:])
      if mx < c:
        mx, mxi = c, i
    a[mxi] += step
    u -= step

  #print(a)
  return ans(k, a)

zn = int(input())
for zi in range(zn):
  print('Case #%d: %.9f'%(zi+1, solve()))

