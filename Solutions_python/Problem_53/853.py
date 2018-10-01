import math
import sys

def snapper(nLights, kSnaps):
    
    rem = kSnaps % math.pow(2, nLights)
    return rem == math.pow(2, nLights) - 1
    

case = 1

for line in sys.stdin.readlines()[1:]:
    vals = line.split(' ')
    n = int(vals[0])
    k = int(vals[1])
    
    if snapper(n,k):
        print "Case #%d: ON" % case
    else:
        print "Case #%d: OFF" % case

    case+=1

