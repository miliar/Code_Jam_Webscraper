T = int( input() )
for Ti in range( 1, T+1 ):
    a1 = int( input() ) - 1
    grid1 = [ [ int(v) for v in input().split() ] for i in range(4) ]
    a2 = int( input() ) - 1
    grid2 = [ [ int(v) for v in input().split() ] for i in range(4) ]

    count = 0
    answer = -1

    for i in range(4):
        for j in range(4):
            if grid1[a1][i] == grid2[a2][j]:
                count += 1
                answer = grid1[a1][i]

    if count == 0:
        print( "Case #{0}: Volunteer cheated!".format(Ti) )
    elif count == 1:
        print( "Case #{0}: {1}".format( Ti, answer ) )
    else:
        print( "Case #{0}: Bad magician!".format(Ti) )