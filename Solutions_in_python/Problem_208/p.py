from queue import PriorityQueue

T = int( input() )
for ti in range( 1, T + 1, 1 ):
  N, Q = map( int, input().split() )
  E = []
  S = []
  for i in range( N ):
    e, s = map( int, input().split() )
    E.append( e )
    S.append( s )
  adj = [ [] for i in range( N ) ]
  for i in range( N ):
    adj[ i ] = list( map( int, input().split() ) )
  dis = [ [ int( 1e15 ) for i in range( N ) ] for j in range( N ) ]
  for i in range( N ):
    for j in range( N ):
      if adj[ i ][ j ] == -1:
        dis[ i ][ j ] = int( 1e15 )
      else:
        dis[ i ][ j ] = adj[ i ][ j ]
      if i == j:
        dis[ i ][ j ] = 0
  for k in range( N ):
    for i in range( N ):
      for j in range( N ):
        dis[ i ][ j ] = min( dis[ i ][ j ], dis[ i ][ k ] + dis[ k ][ j ] )
  ans = []
  for qi in range( Q ):
    st, ed = map( int, input().split() )
    st -= 1
    ed -= 1
    dp = [ [ 1e15 for i in range( N ) ] for j in range( N ) ]
    dp[ st ][ st ] = 0.0
    pq = PriorityQueue()
    pq.put( [ 0.0, st, st ] )
    while not pq.empty():
      d, u, h = pq.get()
      if dp[ u ][ h ] != d: continue
      if u == ed: break
      e = E[ h ] - dis[ h ][ u ]
      for v in range( N ):
        if u == v: continue
        if dis[ u ][ v ] > e: continue
        if dp[ v ][ h ] > d + dis[ u ][ v ] / S[ h ]:
          dp[ v ][ h ] = d + dis[ u ][ v ] / S[ h ]
          pq.put( [ dp[ v ][ h ], v, h ] )
        if dp[ v ][ v ] > d + dis[ u ][ v ] / S[ h ]:
          dp[ v ][ v ] = d + dis[ u ][ v ] / S[ h ]
          pq.put( [ dp[ v ][ v ], v, v ] )
    ans.append( min( dp[ ed ] ) )
  print( "Case #%d: " % ti, end = "" )
  for i in range( Q ):
    print( "%.7f " % ans[ i ], end = "" )
  print()
