def solve( A, B ):
   results = set()
   l = len( str(A) )
   for I in range( A, B+1 ):
      #print I
      for j in range(l):
         strI = str(I)
         strC = strI[j:] + strI[:j]
         C = int( strC )
         if I != C and A <= C and C <= B:
            results.add( ( min( I, C ), max( I, C ) ) )
            #print "strI={}, strC={}".format( strI, strC )
   #print results
   return len( results )

from sys import stdin
T = int( stdin.readline() )
for i in range(T):
   tokens = stdin.readline().split()
   A = int( tokens[0] )
   B = int( tokens[1] )
   #print "A={}, B={}".format( A, B )
   print "Case #{}: {}".format( i+1, solve( A, B ) )
