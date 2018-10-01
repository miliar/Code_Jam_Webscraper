import sys
from math import sqrt, floor, ceil
fname = sys.argv[1]
with open(fname) as fp:
    cont = [line for line in fp]

mag = int(cont[0])
cont = cont[1:]

def palindrome(subject):
    h, t = 0, len(subject)-1
    while(h<=t):
        if(subject[h]!=subject[t]):
            return False
        h+=1
        t-=1
    return True

for case in range(1, mag+1):
    llim, ulim = [int(i) for i in cont[0].split()]
    llim, ulim = int(ceil(sqrt(llim))), int(floor(sqrt(ulim)))
    found = 0
    for i in range(llim, ulim+1):
        if palindrome(str(i)) and palindrome(str(i**2)):
            found +=1
    print "Case #%s: %s" % ( case, found )

    cont = cont[1:]
