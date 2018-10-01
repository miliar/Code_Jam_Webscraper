

def solve(d, k_s):
    """Reach goal d without overtaking any horse (k, s) in k_s"""
    arrival = max([(d - k) / s for k, s in k_s])
    return d / arrival

t = int(input())
for i in range(1, t + 1):
  d, n = map(int, input().split(" "))
  k_s = [None] * n
  for j in range(n):
      k_s[j] = [int(c) for c in input().split(" ")]
  print("Case #{}: {}".format(i, solve(d, k_s)))
