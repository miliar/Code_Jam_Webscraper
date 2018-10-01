inf  = open( 'C-small-1-attempt1.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    N, K = map( int, inf.readline().split(' ') )
    ans = 0
    U = float( inf.readline() )
    p = map( float, inf.readline().split( ' '  ) )
    p.sort()
    i = 0

    while i < N:
        #print p
        upd = False
        j = i
        while j < N and p[j] == p[i]:
            j += 1

        nextp = 1.0
        if j < N:
            nextp = p[j]
        if p[i] == nextp:
            break
        if ( nextp - p[i] ) * ( j - i ) < U:
            U -= (nextp - p[i]) * (j - i)
            for k in xrange( i, j ):
                p[k] = nextp
            upd = True
        else:
            up = U / ( j - i ) + p[i]
            for k in xrange( i, j ):
                p[k] = up
            break
        if not upd:
            break

    prob = 1.0
    for i in xrange( N ):
        prob *= p[i]


    outf.write('Case #%d: %.9f\n' % (caseId, prob ))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )