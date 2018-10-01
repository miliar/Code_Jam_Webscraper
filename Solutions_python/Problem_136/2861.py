T = int(raw_input())

def solve(case):
  [c,f,x] = map(float, raw_input().split(' '))
  best = x/2
  ttb = c/2
  prod = 2 + f
  n = 1

  while ttb + x/prod < best:
    best = ttb + x/prod
    ttb += c/(2+n*f)
    n += 1
    prod = 2 + n * f

  print "Case #%d: %.6f" % (case, best)


for i in xrange(1,T+1): solve(i)
      
