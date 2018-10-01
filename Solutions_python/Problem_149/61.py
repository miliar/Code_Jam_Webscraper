# python3
T = int(input())
for t in range(1, T + 1):
  N = int(input())
  A = list(map(int, input().split()))
  MA = list(A)
  MA.sort()
  ans = 0
  for ma in MA:
    idx = A.index(ma)
    ans += min(idx, len(A) - 1 - idx)
    A = A[:idx] + A[idx + 1: ]
  print("Case #{}: {}".format(t, ans))

