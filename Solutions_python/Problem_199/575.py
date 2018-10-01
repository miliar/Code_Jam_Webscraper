inf  = open( 'A-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    seq, k = inf.readline().split(' ')
    seq = list( seq )
    print seq, k
    k = int( k )
    ans = 0
    for left in xrange( len(seq) - k + 1 ):
        if seq[ left ] == '-':
            ans += 1
            for i in xrange( left, left + k ):
                seq[ i ] = '+' if seq[ i ] == '-' else '-'
    if sum( c == '-' for c in seq ) > 0:
        ans = 'IMPOSSIBLE'
    else:
        ans = str( ans )

    outf.write('Case #%d: %s\n' % (caseId, ans))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )