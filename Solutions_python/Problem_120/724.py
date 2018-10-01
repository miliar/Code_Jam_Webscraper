import sys
import math

def docase(f,k):
  data = f.next().split()
  r = int(data[0])
  t = int(data[1])
  temp = (-(2*r-1)+math.sqrt(pow(2*r-1,2)+8*t))/4
  res = int(math.floor(temp))
  #cnt = 0
  #q = 0
  #while q <= t:
  #  #print str(q)+ 'test' + str(t)
  #  cnt += 1
  #  q += pow(r+2*(cnt-1)+1,2)-pow(r+2*(cnt-1),2)
  #cnt -= 1
  print "Case #" + str(k+1) + ": " + str(res)

with open(sys.argv[1],"r") as f:
  T = int(f.next())
  for k in xrange(T):
    docase(f,k)