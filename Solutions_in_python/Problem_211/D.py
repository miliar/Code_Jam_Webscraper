import os,sys,itertools,math,collections,string
sys.setrecursionlimit(10**7)

def calc(min_k, probs):
  n = len(probs)
  dp = []
  for _ in range(n+1):
    dp.append([0.0] * (n + 1))
  dp[0][0] = 1.0
  for k in range(n+1):
    for i in range(1,n+1):
      p = 0.0
      p += dp[k][i-1] * (1.0 - probs[i-1])
      if k > 0:
        p += dp[k-1][i-1] * probs[i-1]
 
      dp[k][i] = p
 
  res = 0.0
  for k in range(min_k, n+1):
    res += dp[k][n]
  return res
 
def upfill(probs, U, start_index):
  n = len(probs)
  tlft = U
  for i in range(start_index, n):
    if i + 1 < n:
      d = probs[i+1] - probs[i]
    else:
      d = 1.0 - probs[i]
    add = min(d, tlft / (i - start_index + 1))
    for k in range(start_index, i+1):
      probs[k] += add
      tlft -= add
    if tlft <= 0.0:
      break;
  return probs
 
def downfill(probs, U):
  n = len(probs)
  tlft = U
  for i in range(n-1, -1, -1):
    if probs[i] + tlft >= 1.0:
      tlft -= 1.0 - probs[i]
      probs[i] = 1.0
    if tlft <= 0.0:
      break
  return probs
 
def solve(K, U, probs):
  n = len(probs)
  best_prob = 0.0
  for fill_down in [False, True]:
    p = sorted(list(probs))
    tlft = U
    if fill_down:
      p = downfill(p, tlft)
      tlft = sum(probs) + U - sum(p)
    for start_index in range(n):
      t = upfill(list(p), tlft, start_index)
      best_prob = max(best_prob, calc(K, t))
  return best_prob
 
def tokgen(f):
  for line in f:
    for token in line.split():
      yield token
 
def main():
  in_iter = tokgen(sys.stdin)
 
  num_cases = int(next(in_iter))
 
  for i in range(num_cases):
    N = int(next(in_iter))
    K = int(next(in_iter))
    U = float(next(in_iter))
    probs = [float(next(in_iter)) for _ in range(N)]
 
    res = solve(K, U, probs)
 
    print('Case #{0}: {1}'.format(i + 1, res)) 

main()