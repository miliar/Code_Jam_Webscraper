T = int(raw_input())

for t in xrange(1,T+1):
    D, N = map(int, raw_input().split())
    hours = []
    
    for _ in xrange(N):
        tempK, tempS = map(int, raw_input().split())
        tempH = (D-tempK)*1.0/tempS
        hours.append(tempH)

    print "Case #{}: {}".format(t, D/max(hours)*1.0)
