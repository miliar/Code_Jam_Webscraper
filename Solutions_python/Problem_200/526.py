for t in xrange(input()):
    n = map(int, list(raw_input()))
    l = len(n)
    print "Case #" + str(t+1) + ":",
    
    for i in xrange(len(n)-1, 0, -1):
        if n[i] < n[i-1]:
            n[i-1] -= 1
            for j in xrange(i, l):
                n[j] = 9
            l = i
    if not n[0]: del n[0]
    
    print ''.join(map(str, n))