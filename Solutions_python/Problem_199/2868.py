import sys
t=input()
def solve(s, k):
  a = map(lambda c: 0 if c == '-' else 1, s)
  res = 0
  for i in range(len(s) - k + 1):
    if a[i] == 0:
      res += 1
      for j in range(i, i + k):
        a[j] = 1 - a[j]
  return str(res) if all(map(lambda c:c==1,a[-k:])) else "IMPOSSIBLE"

for i in range(t):
  s = raw_input().split()
  print "Case #%d: %s" % (i + 1, solve(s[0], int(s[1])))
