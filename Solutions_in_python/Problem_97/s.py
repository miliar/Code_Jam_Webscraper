import sys

p = sys.argv[1]
f = open(p)
n = int(f.readline())

def pairsof(n, b):
  # Generate {m|n<m<=b && ispair(n,m)}
  rv = []
  # Given n with k digits, there are at most k choices for m.
  # Some will be invalid becuase they're too big or too small,
  # and some will be invalid because they have leading zeros.
  sn = str(n)
  for i in range(1, len(sn)):
    cand = sn[i:] + sn[:i]
    if (not cand[0] == '0'):
      c = int(cand)
      if n < c and c <= b:
        rv.append(c)
  return rv

def numpairs(a, b):
  t = {}
  ans = 0
  for n in range(a, b):
    for m in pairsof(n, b):
      if (n,m) not in t:
        t[(n,m)] = True
        ans += 1

  return ans

for l in range(n):
  a, b = f.readline().split(' ')
  ra = int(a)
  rb = int(b)
  a = min(ra, rb)
  b = max(ra, rb)
  np = numpairs(a, b)
  print "Case #%s: %s" % (l + 1, np)

