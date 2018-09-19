import sys

def get_cases( lines ):
    #------------------------------------
    def get_N( line ):
        N = int( line.split( " " )[ 0 ] )
        return N
    #------------------------------------
    cases = []
    case = []
    indicator = 0
    for line in lines:
        indicator -= 1
        if indicator < 0:
            indicator = get_N( line )
        elif indicator == 0:
            case.append( line.split( " " ) )
            cases.append( case )
            case = []
        else:
            case.append( line.split( " " ) )
    return cases

def strip_lines( lines ):
    result = []
    for line in lines:
        result.append( line.strip() )
    return result

def is_greater( str_1, str_2 ):
    if int( str_1 ) > int( str_2 ):
        return True
    else:
        return False

def get_result( case ):
    def check_row( value, row_number, case ):
        for field in case[ row_number ]:
            if is_greater( field, value ):
                return "NO"
        return "YES"
    def check_column( value, col_number, case, N ):
        for i in range( N ):
            if is_greater( case[ i ][ col_number ], value ):
                return "NO"
        return "YES"
    N = len( case )
    M = len( case[ 0 ] )
    for i, row in enumerate( case ):
        for j, value in enumerate( row ):
            if check_row( value, i, case ) == "NO" and check_column( value, j, case, N ) == "NO":
                return "NO"
    return "YES"
            
lines = []
with open( sys.argv[ -1 ], "r" ) as f_in:
    lines = f_in.readlines()
    lines = strip_lines( lines[ 1 : ] )

cases = get_cases( lines )
for index, case in enumerate( cases ):
    print "Case #{0}: {1}".format( index + 1, get_result( case ) )
