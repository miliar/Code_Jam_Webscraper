def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def dictadd(dct, key, val):
  if not dct.has_key(key):
    dct[key] = val
  else:
    dct[key] += val
  
def call():
  dist, k = [int(i) for i in raw_input().split()]
  maxtime = 0.0
  for i in range(k):
    pos, speed = [float(i) for i in raw_input().split()]
    time = (dist - pos) / speed
    if time > maxtime:
      maxtime = time
  finalspeed = float(dist) / maxtime
  return finalspeed
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())