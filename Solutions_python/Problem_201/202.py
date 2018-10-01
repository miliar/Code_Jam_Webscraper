memory = {}

def solve(n, k):
  key = '%s %s' % (n, k)
  if key in memory:
    return memory[key]

  r = (n-1)//2
  if k == 1:
    return [n-1-r, r]
  b = (k-1)//2
  x = solve(n-1-r, k-1-b)
  y = solve(r, b) if b > 0 else x
  memory[key] = [min(x[0], y[0]), min(x[1], y[1])]
  return memory[key]

t = int(input())
for i in range(1, t+1):
  [n, k] = map(int, input().split(' '))
  print("Case #%s: %s" % (i, ' '.join(map(str, solve(n, k)))))
