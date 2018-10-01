"""
Clive Gifford's Solution to the "Fly Swatter" problem, GCJ 2008
"""

import sys, math

try:
   import psyco
   psyco.full()
except:
   print "Can't import psyco"     

def SegArea(y, Radius):
   theta = 2 * math.acos(y / Radius)
   return Radius * Radius / 2.0 * (theta - math.sin(theta))
   
def SegDiffs(y1, y2, Radius):
   return (SegArea(y2, Radius) - SegArea(y1, Radius)) / 2.0
   
def Probability(f, R, t, r, g):
#   print f,R,t,r,g
   gridInc = g + 2 * r
   gapSize = g - 2 * f
   if gapSize <= 0: return 1.0
   innerRadius = R - t - f   # Max distance fly midpoint can be from centre (origin)
   innerRadiusSquared = innerRadius * innerRadius
   innerArea = math.pi * innerRadiusSquared
   complete = 0
   partialSafe = 0.0
   yB = r + f
   yT = yB + gapSize
   while yB < innerRadius:
      xL = r + f     
      xR = xL + gapSize
      while xL < innerRadius:
         if (xR * xR + yT * yT) <= innerRadiusSquared:
            complete += 1 
         elif (xL * xL + yB * yB) < innerRadiusSquared:
            if xL * xL + yT * yT <= innerRadiusSquared:
               inTL = True
            else:
               inTL = False   
            if xR * xR + yB * yB <= innerRadiusSquared:
               inBR = True
            else:
               inBR = False  
            if inTL and inBR:
               x1 = math.sqrt(innerRadiusSquared - yT * yT) 
               y1 = yT
               x2 = xR
               y2 = math.sqrt(innerRadiusSquared - xR * xR) 
               partialSafe += gapSize * (y2 - yB)
               partialSafe += SegDiffs(y1, y2, innerRadius) - xL * (y1 - y2)
            elif inTL and not inBR:
               x1 = math.sqrt(innerRadiusSquared - yT * yT) 
               y1 = yT
               x2 = math.sqrt(innerRadiusSquared - yB * yB) 
               y2 = yB
               partialSafe += SegDiffs(y1, y2, innerRadius) - xL * (y1 - y2)
            elif not inTL and inBR:
               x1 = xL
               y1 = math.sqrt(innerRadiusSquared - xL * xL) 
               x2 = xR
               y2 = math.sqrt(innerRadiusSquared - xR * xR) 
               partialSafe += gapSize * (y2 - yB)
               partialSafe += SegDiffs(y1, y2, innerRadius) - xL * (y1 - y2)
            else:
               x1 = xL
               y1 = math.sqrt(innerRadiusSquared - xL * xL) 
               x2 = math.sqrt(innerRadiusSquared - yB * yB) 
               y2 = yB
               partialSafe += SegDiffs(y1, y2, innerRadius) - xL * (y1 - y2)
         xL += gridInc
         xR += gridInc  
      yB += gridInc
      yT += gridInc  

   outerArea = math.pi * R * R / 4.0      # We have looked at one quadrant only
   innerSafe = complete * gapSize * gapSize + partialSafe
   return 1.0 - innerSafe / outerArea
   
def main():
   fin = file(sys.argv[1])
   fout = file(sys.argv[2], "wt")

   numCases = int(fin.readline())
   for case in xrange(numCases):
      f, R, t, r, g = map(float, fin.readline().split())
      fout.write("Case #%d: %f\n" % (case+1, Probability(f, R, t, r, g)))
   
if __name__ == "__main__":
   main()   
   