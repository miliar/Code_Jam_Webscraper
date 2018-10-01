from __future__ import division

T = input()

for i in range(T):
  C, F, X = [float(x) for x in raw_input().split()]

  cookiesRate = 2

  if C >= X : print "Case #%d: %.7f" % (i+1, X/cookiesRate)
  
  else:
    timeElapsed = 0

    while(C/cookiesRate + X/(cookiesRate+F) < X/cookiesRate): 
      timeElapsed += C/cookiesRate
      cookiesRate += F

    timeElapsed += X/cookiesRate

    print "Case #%d: %.7f" % (i+1, timeElapsed)