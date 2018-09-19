from math import sqrt, floor

f = open("A-small-attempt0.in","r")
numTests = int(f.readline())

for test in range(numTests):

  data = f.readline().strip().split()
  r = long(data[0])
  t = long(data[1])

  n = 1.0/4.0*(sqrt(8*t+4*r*(r-1)+1) - 2*r + 1)
  print "Case #%i: %i" % (test+1,int(floor(n)))
