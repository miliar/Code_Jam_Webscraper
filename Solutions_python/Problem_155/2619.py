import sys
with open(sys.argv[1]) as f:
  t = int(f.readline().strip())
  s = []
  for l in f:
    s.append(map(int, list(l.strip().split()[1])))

def test(s):
  x = [0]
  z = []
  for i, y in enumerate(s[:-1]):
    x.append(x[-1]+y)
    z.append(i+1-x[-1])

  if len(z) == 0:
    return 0
  else:
    return max(z) if max(z) > 0 else 0

for i, x in enumerate(s):
  print "Case #{}: {}".format(i+1, test(x))
