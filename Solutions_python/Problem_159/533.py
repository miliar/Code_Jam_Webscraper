import sys
import math

lines = sys.stdin.read().split('\n')

for k in range( 0, int(lines[0]) ):
  sys.stdout.write( 'Case #' + str(k+1) + ': ' )

  vec = map( int, lines[ k*2+2 ].split(' ') )

  #print( vec )

  vec2 = []
  for l in range(0, len(vec)-1):
    if vec[l]<vec[l+1]:
      vec2.append( 0 )
    else:
      vec2.append( vec[l]-vec[l+1] )
  #min2 = max(vec2) * (len(vec)-1) + vec[len(vec)-1]
  #minvec2 = min(vec2)
  #min1 = minvec2*(len(vec)-1)
  min1 = sum( vec2 )
  #for l in range(0, len(vec)-1):
  #  min1 = min1 + min(vec[l],minvec2)
  sys.stdout.write( str( min1) + ' ' )

  vec2 = []
  for l in range(0, len(vec)-1):
    vec2.append( vec[l]-vec[l+1] )
  #min2 = max(vec2) * (len(vec)-1) + vec[len(vec)-1]
  maxvec2 = max(vec2)
  min2 = 0
  for l in range(0, len(vec)-1):
    min2 = min2 + min(vec[l],maxvec2)
  sys.stdout.write( str( min2) )

  print('')
