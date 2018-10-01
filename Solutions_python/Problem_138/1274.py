import bisect

def line(f):
  return f.readline().strip()

i = open("D-large.in", "r")
o = open("2.out", "w")

T = int(line(i))

def dwar(a, b):
  r = 0
  while len(b):
    idx = bisect.bisect(a, b[0])
    if idx != len(a):
      r += 1
      del a[idx]
      del b[0]
    else:
      break;
  return r

def war(a, b):
  r = 0
  n = len(a)
  while len(a):
    idx = bisect.bisect(b, a[0])
    if idx != len(b):
      r += 1
      del b[idx]
      del a[0]
    else:
      break;
  return n-r

for t in xrange(T):
  n = int(line(i))
  naomi = map(float, line(i).split())
  ken = map(float, line(i).split())
  naomi.sort()
  ken.sort()
  assert(len(naomi) == len(ken))
  r1 = dwar(naomi[:], ken[:])
  r2 = war(naomi[:], ken[:])
  print>>o, "Case #%d: %d %d" % (t+1, r1, r2)
