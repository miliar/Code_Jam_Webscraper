fi = open('B-large.in','r')
t = int(fi.readline())
for i in xrange(0, t):
  C, F, X = map(float, fi.readline().split())
  cps = 2.0
  time = 0.0
  while True:
    if X/cps <= C/cps + X/(cps+F):
      time += X/cps
      break
    else:
      time += C/cps
      cps += F
  print "Case #%d: %f" % (i+1, time)
fi.close
