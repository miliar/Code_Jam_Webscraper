from collections import deque

def solve(S, k):
  ls = len(S)
  q = deque()
  q.append((S, 0))
  e = set()

  while q:
    ss, n = q.popleft()

    if ss.count('+') == ls:
      return n

    if "".join(ss) in e:
      continue

    e.add("".join(ss))

    for i in xrange(0, ls-k+1):
      s = list(ss)
      for j in xrange(i, i+k):
        if s[j] == '-':
          s[j] = '+'
        else:
          s[j] = '-'

      q.append((s, n+1))

  return "IMPOSSIBLE"

with open("A-small-attempt0.in") as f:
  nc = int(f.readline().strip())
  for c in range(0, nc):
    S, k = f.readline().strip().split(" ")
    print("Case #{}: {}".format(c+1, solve(list(S), int(k))))