import sys

def solve( filename ):
  file = open( filename, 'r' )
  
  tests = int( file.readline() )
  
  for i in range(tests):
    bits = [int(x) for x in file.readline().split()]
    n = bits[0]
    l = bits[1]
    h = bits[2]
    others = [int(x) for x in file.readline().split()]

    for note in range(l,h+1):
            if sum( [ max([x,note])%min([x,note]) for x in others ] ) == 0:
              print( "Case #{0}: {1}".format(i+1, note))
              break
            elif note == h:
              print( "Case #{0}: {1}".format(i+1, "NO"))


solve( sys.argv[1] )  
