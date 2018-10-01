import math

cases = raw_input()
for i in range(1,int(cases)+1):
  [r,t] = raw_input().split(" ")
  r = int(r)
  t = int(t)
  
  #ifor i in range(1,3)
  
  rings = math.floor((-3 - r*2 + math.sqrt((3 + 2*r)**2 - 8*(2*r + 1 - t)))/4 )
  
  if (2 * rings**2 + (3+2*r) * rings + 2*r + 1) > t:
    rings = int(rings)-1
  else:
    rings = int(rings) 
    
  print "Case #{0}: {1}".format(i,int(rings)+1)
