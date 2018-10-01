from sys import stdin

T = int(stdin.readline())

for tc in xrange(1, T+1):
  X, R, C = (int(a) for a in stdin.readline().split())
  if R > C:
    R, C = C, R

  richard = "RICHARD"
  gabriel = "GABRIEL"

  result = gabriel

  if X > 6:
    result = richard

  if R == 1 and X > 2:
    result = richard

  if (R*C) % X != 0:
    result = richard
    
  if R < 3 and X > 4:
    result = richard

  if R == 2 and X > 3:
    result = richard

  print "Case #%d: %s" % (tc, result)
     
