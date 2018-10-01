from sys import stdin

n = int(stdin.readline().strip())
for _ in xrange(1,n+1):
    n, k = map(int,stdin.readline().strip().split())
    print "Case #%d: %s"%(_, "ON" if (k & ((1 << n)-1)) == ((1 << n)-1) else "OFF")

