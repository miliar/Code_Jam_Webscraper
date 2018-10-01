from sys import *

def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

ncases = int(stdin.readline())
for z in xrange(1,ncases+1):
    t = map(int,stdin.readline().split())
    T = 0
    for i in xrange(1,len(t)):
        for j in xrange(i+1,len(t)):
            T = gcd(T, abs(t[i]-t[j]))
    ans = T - (t[1]%T)
    if (ans == T): ans = 0
    print "Case #%d: %d" %(z, ans)
