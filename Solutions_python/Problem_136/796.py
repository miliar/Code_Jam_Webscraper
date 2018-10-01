import sys

n = int(input())
for i in range(1, n+1):
  [c, f, x] = [float(s) for s in sys.stdin.readline().strip().split(" ")]
  
  r = 2.0
  total = 0.0
  while True:
    t1 = x/r
    j = c/r
    t2 = j + x/(r+f)
    
    if t2 < t1:
      r += f
      total += j
    else:
      total += t1
      break

  print "Case #%s: %.7f" % (i, total)
