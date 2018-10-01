import numpy as np

# fin = open( 'A-small-practice.in', 'r' )
# fout = open( 'A-small-practice.out', 'w' )

fin = open( 'A-small-attempt3.in', 'r' )
fout = open( 'A-small-attempt3.out', 'w' )

# fin = open( 'A-large-practice.in', 'r' )
# fout = open( 'A-large-practice.out', 'w' )

numTests = int( fin.readline() )
itemlen = np.zeros( (numTests,1) )

for kk in range( 1, numTests + 1 ):
   textline = fin.readline()

   caselist = textline.split()
   simax = caselist[0]
   numstr = caselist[1]
   
   invite = 0
   runtotal = int( numstr[0] )
   for mm in range( 1, len( numstr ) ):
      si = int( numstr[mm] )
      if runtotal >= mm:
         runtotal += si
      else:
         if si == 0:
            continue
         else:
            invite += mm - runtotal
         runtotal += ( si + invite )
      print runtotal

   fout.write( 'Case #' + str( kk ) + ': ' + str( invite ) + '\n' )
   print 'invited ' + str( invite )
   

fin.close()
fout.close()
