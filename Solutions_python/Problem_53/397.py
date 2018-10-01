def bin(n, count=31):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])

import math
def onoff(n, k):
    l = list(bin(k));
    l.reverse()
    if "".join(l)[0:n] == bin(int(math.pow(2, n)) - 1)[-n:]:
        return "ON"
    else:
        return "OFF"
    
import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()

i = 0
for line in lines:
  if i > 0 and len(line) > 1:
   split = line.split(" ") 
   print "Case #" + str(i) + ": " + onoff(int(split[0]), int(split[1]))
  i = i + 1
