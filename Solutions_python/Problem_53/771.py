def snap(N,K):
    if K % 2**N == (2**N - 1):
        return "ON"
    return "OFF"


T = int(raw_input())
for i in xrange(T):
    N, K = [int(x) for x in raw_input().split()]
    print "Case #%d: %s" % (i+1, snap(N,K))
 
