import math

def dt(x1, y1, r1, x2, y2, r2):
  dst = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
  if dst + r1 < r2:
    return r2
  if dst + r2 < r1:
    return r1
  return (dst + r1 + r2) * 0.5

f = open('p4.in', 'r')
T = int(f.readline())
for tno in range(T):
  n = int(f.readline())
  x = []
  y = []
  r = []
  for i in range(n):
    X, Y, R = [int(z) for z in f.readline().split(' ')]
    x.append(X)
    y.append(Y)
    r.append(R)
  if n == 1:
    sol = r[0]
  elif n == 2:
    sol = max(r[0], r[1])
  else:
    sol = max(dt(x[0], y[0], r[0], x[1], y[1], r[1]), r[2])
    sol = min(sol, max(dt(x[0], y[0], r[0], x[2], y[2], r[2]), r[1]))
    sol = min(sol, max(dt(x[2], y[2], r[2], x[1], y[1], r[1]), r[0]))
  print 'Case #%s: %.6f' % (tno + 1, sol)
