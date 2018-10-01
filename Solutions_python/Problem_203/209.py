nt = int(raw_input())

for i_it in xrange(nt):
    nr,nc = map(int,raw_input().split())
    m = []
    for i in xrange(nr):
        m.append(map(str,raw_input()))
        
    for i in xrange(nr):
        cf = '?' 
        fir = True
        for j in xrange(nc):
            if m[i][j] != '?':
                cf = m[i][j]
                if fir:
                    fir = False
                    m[i][0:j] = j*cf                    
            m[i][j] = cf        
        
    for i in xrange(nr):
        if i > 0 and m[i][0] == '?':
            m[i] = list(m[i-1])
    
    for i in xrange(nr,-1,-1):
        if i < nr-1 and m[i][0] == '?':
            m[i] = list(m[i+1])
                        
    print "Case #{}:".format(i_it+1)
    for i in xrange(nr): print ''.join(m[i])