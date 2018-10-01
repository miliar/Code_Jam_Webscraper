import fractions, itertools, sys

def lcm(a, b):
  return a * b / fractions.gcd(a, b)

def b(j, n, ts):
  ts.sort()
  diffs = [b - a for a, b in itertools.combinations(ts, 2)]
  gcd = diffs[0]
  if len(diffs) > 1:
    for i in range(1, len(diffs)):
      gcd = fractions.gcd(gcd, diffs[i])
  #print gcd
  
  for t in ts:
    if t % gcd != 0:
      break
  else:
    print 'Case #%d: 0' % j
    return
  
  m = ts[-1] % gcd
  i = gcd - m
  while True:
    k = 0
    while k < n:
      if (ts[k] + i) % gcd != 0:
        i += gcd
        k = 0
        continue
      k += 1

    print 'Case #%d: %d' % (j, i)
    break
  
if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    c = int(f.readline())
    for j in range(1, c + 1):
      l = [int(x) for x in f.readline().split()]
      n, ts = l[0], l[1:]
      b(j, n, ts)
