f = open('a.in','r')
o = open('a.out','w')

T = int(f.readline())

for i in xrange(T):
    o.write('Case #' + str(i+1) + ':\n')

    N = int(f.readline())
    I = [f.readline() for i in xrange(N)]
        
    WP = []
    for i in xrange(N):
        WP.append( [0 for i in xrange(N)] )

    for i in xrange(N):
        a = b = 0
        for j in xrange(N):
            if I[i][j] != '.':
                a += int(I[i][j])
                b += 1
        WP[i][i] = 1. * a / b    
        for j in xrange(N):
            if I[i][j] == '1':
                WP[i][j] = 1. * (a-1) / (b-1)
            elif I[i][j] == '0':
                WP[i][j] = 1. * a / (b-1)
            else :
                WP[i][j] = 1. * a / b

    OWP = [0 for i in xrange(N)]
    for i in xrange(N):
        a = 0
        b = 0
        for j in xrange(N):
            if j != i and I[i][j] != '.':
                a += WP[j][i]
                b += 1
        OWP[i] = a / b

    for i in xrange(N):
        a = 0
        b = 0
        for j in xrange(N):
            if I[i][j] != '.': 
                a += OWP[j]
                b += 1
        o.write( str( .25 * WP[i][i] + .5 * OWP[i] + .25 * a / b ) + '\n')
