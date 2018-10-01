import string
import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def isPossible(N,pD,PG):
    gc = gcd(pD,100)
    D = 100/gc
    if (D>N):
        return False
    if((pD != 100)and (pG == 100)):
        return False
    if((pD != 0)and(pG == 0)):
        return False
    return True

f =open(sys.argv[1],"r")
T =int(f.readline())

for i in range (T):
    inp = f.readline().split()
    N= int(inp[0])
    pD = int(inp[1])
    pG = int(inp[2])
    
    if(isPossible(N,pD,pG)):
        print "Case #{0}: {1}".format(i+1,"Possible")
    else:
        print "Case #{0}: {1}".format(i+1,"Broken")
