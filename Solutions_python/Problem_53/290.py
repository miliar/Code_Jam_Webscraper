T = int(raw_input())
for t in xrange(T):
    N, K = map(int, raw_input().split())
    print "Case #%d:"%(t+1), ("OFF", "ON")[((K+1)%(1<<N)==0)]
