for t in xrange(input()):
    d, n = map(int, raw_input().split())
    y = float("inf")
    
    print "Case #" + str(t+1) + ":",
    for i in xrange(n):
        k, s = map(int, raw_input().split())
        c = s *1. / (d-k) * d
        if c < y: y = c
    
    print "%.6f" % y