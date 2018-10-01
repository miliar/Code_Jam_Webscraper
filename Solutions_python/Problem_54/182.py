from sys import stdin
from fractions import gcd

n = int(stdin.readline().strip())
for _ in xrange(1,n+1):
    t = map(int,stdin.readline().strip().split())[1:]
    T = abs(t[0] - t[1])
    for i in xrange(1,len(t)-1): T = gcd(T, abs(t[i+1] - t[i]))
    print "Case #%d: %d"%(_, (T - (t[0] % T)) % T)
