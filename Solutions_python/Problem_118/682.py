from math import sqrt
halflen = lambda t: (len(t)+1)/2
def paliroot(n, up):
  t = str(int(sqrt(n)))
  if up != (len(t) % 2 == 0):
    return int(t[:halflen(t)])
  if not up: return 10**(len(t)/2)
  return 10**(len(t)/2) - 1
def palisquare(n, up):
  t = str(n)
  r = t[::-1]
  return int(t+r[not up:])**2
def palitest(n):
  t = str(n)
  h = halflen(t)
  return t[:h] == t[-h:][::-1]
def myxrange(i,j):
  while i<j:
    yield i
    i += 1
def force(a,b):
  global proof
  proof = []
  count = 0
  for i in myxrange(a,b+1):
    x = sqrt(i)
    if x.is_integer() and palitest(i) and palitest(int(x)):
      count += 1
      proof += [i]
  return count
fi = open('C-large-1.in')
fo = open('C-large-1.out', 'w')
for i in range(1, eval(fi.readline())+1):
  a, b = map(int, fi.readline().split())
  #print i
  #a,b = i, 10**10
  #brute = force(a,b)
  lo = paliroot(a, False)
  hi = paliroot(b, True)
  ans = 0
  for j in xrange(lo, hi+1):
    for up in False, True:
      p = palisquare(j, up)
      if a <= p <= b and palitest(p):
        ans += 1
        #print p
  #assert len(ans) == brute
  print >>fo, 'Case #%i:'%i, ans
del fo
