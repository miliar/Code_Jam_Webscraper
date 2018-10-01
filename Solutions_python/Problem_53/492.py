from mfw import mfw

infile = 'A-large.in'

with mfw( ( infile, 'r' ), ( '%s.out' % infile[:-3], 'w' ) ) as ( fhi, fho ):

    # 1st line is number of cases.
    cases = int( fhi.readline() )

    for case in range( cases ):
      # N Snappers, K Snaps.
      N, K = map( int, fhi.readline().rstrip().split( ' ' ) )

      # No Snaps - No power.
      if K == 0:
        res = 'OFF'

      # 1 Snapper = Odd / Even Check.
      elif N == 1:
        if K % 2 == 0:
          res = 'OFF'
        else:
          res = 'ON'

      # > 1 Snapper - Light is only on if all Snappers are on.
      else:
        if K % ( 2 ** N ) == 2 ** N - 1:
          res = 'ON'
        else:
          res = 'OFF'

      fho.write( 'Case #%d: %s\n' % ( case + 1, res ) )
