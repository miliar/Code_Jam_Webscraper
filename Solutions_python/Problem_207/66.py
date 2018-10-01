T = int( input() )
for ti in range( 1, T + 1, 1 ):
  N, R, O, Y, G, B, V = map( int, input().split() )
  mxid = 0
  if R == max( R, Y, B ): mxid = 0
  elif Y == max( R, Y, B ): mxid = 1
  else: mxid = 2
  sss = ""
  if R + Y + B - max( R, Y, B ) < max( R, Y, B ):
    sss = "IMPOSSIBLE"
  else:
    for i in range( max( R, Y, B ) ):
      if mxid == 0:
        sss += "R"
        if Y > B:
          Y -= 1
          sss += "Y"
        elif Y <= B:
          B -= 1
          sss += "B"
        while i + 1 == max( R, Y, B ) and Y + B > 0:
          if Y >= B and sss[ len( sss ) - 1 ] != 'Y':
            Y -= 1
            sss += "Y"
          elif B >= Y and sss[ len( sss ) - 1 ] != 'B':
            B -= 1
            sss += "B"
          else:
            break
      elif mxid == 1:
        sss += "Y"
        if R > B:
          R -= 1
          sss += "R"
        elif R <= B:
          B -= 1
          sss += "B"
        while i + 1 == max( R, Y, B ) and R + B > 0:
          if R >= B and sss[ len( sss ) - 1 ] != 'R':
            R -= 1
            sss += "R"
          elif B >= R and sss[ len( sss ) - 1 ] != 'B':
            B -= 1
            sss += "B"
          else:
            break
      else:
        sss += "B"
        if Y > R:
          Y -= 1
          sss += "Y"
        elif Y <= R:
          R -= 1
          sss += "R"
        while i + 1 == max( R, Y, B ) and Y + R > 0:
          if Y >= R and sss[ len( sss ) - 1 ] != 'Y':
            Y -= 1
            sss += "Y"
          elif R >= Y and sss[ len( sss ) - 1 ] != 'R':
            R -= 1
            sss += "R"
          else:
            break
  if len( sss ) != N:
    sss = "IMPOSSIBLE"
  print( "Case #%d: %s" % ( ti, sss ) )
