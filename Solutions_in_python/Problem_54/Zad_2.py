import numpy

def _euclid(a):
   if a.shape[0]==1:
      return a[0]
   eu = a[0]
   for x in a[1:]:
      eu = euclid(eu, x)
   return eu

def euclid(numA, numB):
   while numB != 0:
      numRem = numA % numB
      numA = numB
      numB = numRem
   return numA


zad = open("B-large.in").read()
z = zad.split('\n')

o = open("out.txt",'w')

try:
   for l in xrange(1,len(z)):
      znj = z[l].split()
      zn = [int(p) for p in znj[1:]]
      a = numpy.array(zn)
      a.sort()
      
      Min = a[0]
      a = a-Min
      
      e = _euclid(a[1:])
      
      #print (e-(Min%e))%e
      o.write("Case #%d: %d\n" % (l,(e-(Min%e))%e))
      
except:
   print "nana"
   
print "ok"

   