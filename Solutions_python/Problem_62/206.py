f = open( "A-large.in" )


caseCount = int( f.readline() )

for caseIndex in xrange( caseCount ):
    lineCount = int( f.readline() )
    lineCollection = []
    for _ in xrange( lineCount ):
        lineCollection.append( map( int , f.readline().split(' ') ) )

    intersectionCount = 0
    totalLine = len( lineCollection )
    for index in xrange( totalLine ):
        for checkIndex in xrange( index + 1 , totalLine ):
            line1 = lineCollection[index]
            line2 = lineCollection[checkIndex]
            if ( line1[0] - line2[0] ) * ( line1[1] - line2[1] ) < 0:
                intersectionCount += 1

    print "Case #%d: %d" % ( caseIndex + 1 , intersectionCount )
