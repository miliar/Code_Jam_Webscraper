#!/usr/bin/env python
import sys, math

def xfromy(R, y):
  return math.sqrt(R**2 - y**2)

def isin(R, p):
  eps = 1e-5
  return p[0] ** 2 + p[1] ** 2 < R ** 2 - eps

def len0(p):
  return math.sqrt(p[0]**2 + p[1]**2)

def getCrossArea3(R, p0, p1, passFirst = False):
  import copy
  retval = 0; a0 = p0; a1 = p1
  if (not passFirst) and (isin(R,p0) ^ isin(R,p1)):
    sign = 1
    if p0[0] != p1[0]:
      p0 = tuple(reversed(p0))
      p1 = tuple(reversed(p1)) # p0 and p1 has common absciss
      sign = -1
    x = p0[0]
    p2 = (x, xfromy(R, x))
    S = getCrossArea3(R, p0, p2, True) +  getCrossArea3(R, p2, p1, True)
    retval =  sign * S
  else:
    vmul =  p0[0] * p1[1] - p0[1] * p1[0]
    if isin(R, p0) or isin(R, p1):
      retval = vmul / 2.0
    else:
      angle = math.asin(vmul / (len0(p0) * len0(p1)))
      retval =  R * R * angle / 2.0
#  print "[%s - %s] => %.4f" % (a0, a1, retval)
  return retval

def getCrossArea4(R, x0, x1, y0, y1):
  p00 = (x0, y0)
  p01 = (x0, y1)
  p10 = (x1, y0)
  p11 = (x1, y1)
  S = getCrossArea3(R, p00, p10) + \
      getCrossArea3(R, p10, p11) + \
      getCrossArea3(R, p11, p01) + \
      getCrossArea3(R, p01, p00)
  return S

def getLineArea(R, y):
  angle = math.asin(y / R)
  x = xfromy(R, y)
  return x * y + angle * R ** 2 

#print getCrossArea4(4, 2, 3, 1, 2)
#print getCrossArea4(4, 3, 4, 1, 2)
#print getCrossArea4(4, 3, 4, 0, 1)
#print getCrossArea4(4, 0, 1, 3, 4)
#print getCrossArea4(4, 30, 31, 0, 1)

def getLineCrossArea(R, y0, y1, p, t):
  x = p
  S = getCrossArea4(R, 0, p, y0, y1)
  while x + t < R:
    tx0 = x + t
    tx1 = tx0 + 2*p
    S += getCrossArea4(R, tx0, tx1, y0, y1)
    x = tx1
  return S  
   
def getSquare(R, p, t):
  if t <= 0:
    return math.pi * R**2
  y = p
  S = getCrossArea4(R, 0, R, 0, p)
  while y < R:
    y0 = y+t
    S += getLineCrossArea(R, y, y0, p, t)
    y1 = y0 + 2 * p
    S += getCrossArea4(R, 0, R, y0, y1)
    y = y1
#  print "%s, %s, %s => %s" % (R, p, t, 4 * S)  
  return 4 * S

def solve(f, R, t, r, g):
  t += f
  S0 = getSquare(R-t, r + f, g - 2 * f)
  S1 = math.pi * (R ** 2 - (R - t) ** 2)
  return (S0 + S1) / (math.pi * R ** 2)

def main():
#  print getCrossArea4(4.0, 0.0, 4.0, 0.0, 0.1)
#  return 0
  #reader = open('c:/temp/gcj/c.in')
  reader = open('c:/temp/gcj/C-small-attempt0.in')
  outAns = sys.stdout #open('out.txt', 'w')
  nTest = int(reader.readline().split()[0])
  for iTest in xrange(1, nTest + 1):
    test = map(float, reader.readline().split())
    print >>outAns, "Case #%d: %.8f" % (iTest, solve(*test))
  return 0

if __name__ == "__main__":
  sys.exit(main())