import sys

a = []
for line in sys.stdin:
    line = line.strip()
    try:
        c, d = line.split(' ')
    except:
        continue
    c = int(c)
    d = int(d)
    a.append((c, d))

def ans(case, maxAns, minAns):
    print 'Case #' + str(case) + ': ' + str(maxAns) + ' ' + str(minAns)
    return case + 1

def f(n, k):
  if k == 1:
    if n % 2 == 1:
      return ((n - 1) / 2, (n - 1) / 2)
    else:
      return (n / 2, (n - 2) / 2)

  if n % 2 == 1:
    return f((n - 1) / 2, k / 2)
  else:
    if k % 2 == 1:
      return f((n - 1) / 2, k / 2)
    else:
      return f(n / 2, k / 2)

case = 1
for (n, k) in a:
  (mx, mn) = f(n, k)
  case = ans(case, mx, mn)
