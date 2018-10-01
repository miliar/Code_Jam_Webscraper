gcd = lambda x, y: x if not y else gcd(y, x%y)

T = int(raw_input(""))

for i in range(1, T+1):
  x = map(int, raw_input("").split(" "))
  N = x[0]
  g = 0
  for j in range(2, N+1):
    g = gcd(g, abs(x[1]-x[j]))
  print "Case #%d: %d" % (i, (-x[1])%g)
