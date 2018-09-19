T = int( input() )
for Ti in range( 1, T+1 ):
    A, B, K = [ int(v) for v in input().split() ]
    r = 0
    for Ai in range(A):
        for Bi in range(B):
            if Ai&Bi < K:
                r += 1

    print( "Case #{0}: {1}".format( Ti, r ) )