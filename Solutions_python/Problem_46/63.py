

test = """3
2
10
11
3
001
100
010
4
1110
1100
1100
1000
"""

test = file( "A-small-attempt2.in" ).read()

ilines = test.split( "\n" )
T = int( ilines[0] )
offset = 1
for t in range( T ):
    N = int( ilines[offset] )

    result = []

    for n in range( N ):
        x = ilines[offset + n + 1]
        try:
            result.append( x.rindex( '1' ) )
        except:
            result.append( 0 )


#    print result
    total = 0
    for n in range( N ):
#        print result
        if result[n] > n:
            oo = [k for k in range( n + 1, N ) if result[k] <= n]
#            print oo
            v = result[oo[0]]

            Xoffset = result.index( v, n + 1 )

#            print n, v, offset, result[n],
            total += Xoffset - n
            result.pop( Xoffset )
            result.insert( n, v )
#            print result

    print 'Case #%s: ' % ( t + 1 ), total

    offset += N + 1


