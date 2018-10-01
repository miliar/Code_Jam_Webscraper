#!/usr/bin/python3

T = int (input ())
for tt in range (T):
  res = 1e100
  (c, f, x) = (float (x) for x in input ().split ())
  speed = 2.0
  cur = 0.0
  for i in range (5 * int (x)):
    #print ('? {0}'.format (res))
    res = min (res, cur + x / speed)
    t = c / speed
    cur += t
    speed += f
  print ('Case #{0}: {1:.7f}'.format (tt + 1, res))
