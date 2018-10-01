import math

def tidy_number( num_array, fw, case ):
    length = len( num_array )
    flip = 1
    for i in range( 1, length ):
        if( num_array[ i ] < num_array[ i - 1 ] ):
            num_array[ i - 1 ] = num_array[ i - 1 ] - 1
            flip = i
            for j in range( i, length ):
                num_array[ j ] = 9
            break

    for j in range( flip - 1, 0, -1 ):
        if( num_array[ j ] < num_array[ j - 1 ] ):
            num_array[ j ] = 9
            num_array[ j - 1 ] = num_array[ j - 1 ] - 1

    number = list( map(lambda x: str( x ), num_array ) )
    number = ''.join( number )
    number = int( number )
    out = "Case #" + str(case) + ": " + str( number )
    fw.write(out)
    fw.write("\n")
    print(out)


f = open('C:\\Users\\nandi\\Desktop\\tidy.txt', 'r')
lines = f.readlines()
i = 0
fw = open( 'C:\\Users\\nandi\\Desktop\\tidy_output.txt', 'w' )

points = []
for line in lines:
    line = line.replace( '\n', '' )
    point = int( line )
    points.append( point )

T = points[ 0 ]

points = points[ 1: ]

case = 1
for point in points:
    p = list( str( point ) )
    p = list( map(lambda x: int( x ), p ) )
    tidy_number( p, fw, case )
    case = case + 1
