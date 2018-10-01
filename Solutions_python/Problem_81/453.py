import sys

def mean(numberList):
    if len(numberList) == 0:
        return float(0)
 
    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)

i = sys.stdin
n = int(i.readline())

for _n in xrange(1,n+1):
  t = int(i.readline())
  results = {}
  for _t in xrange(t): 
    results[_t] = list(i.readline().strip())
  wp = {}
  for g in xrange(t):
    r = map(int,[d for d in results[g] if d in "10"])
    wp[g] = mean(r)
#print mean(r)
  owp = {}
  for g in xrange(t):
    _wp = {}
    owp_l = []
    for h in xrange(t):
      if h!=g:
        if results[g][h] in "10":
          if g==0:
            r = map(int,[d for d in results[h][1:] if d in "10"])
          else:
            r = map(int,[d for d in results[h][:g]+results[h][g+1:] if d in "10"])
          _wp[h] = mean(r)
          owp_l += [_wp[h]]
    owp[g] = mean(owp_l)
  oowp = {}
  for g in xrange(t):
    oowp_l =[]
    for h in xrange(t):
      if g!=h:
        if results[g][h] in "10":
          oowp_l += [owp[h]]
    oowp[g] = mean(oowp_l)
  print "Case #%i:"%_n
  for g in xrange(t):
    print 0.25*wp[g] + 0.5*owp[g] + 0.25*oowp[g]


