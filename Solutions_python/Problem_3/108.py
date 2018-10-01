#!/usr/bin/python
#sorry, ugly code, running out of time
import math
def areac(h,v,dh,R):
   dv=(R**2-v**2)**0.5
   l=((dv-dh)**2+(h-v)**2)**0.5
   sa2=(l/2)/R
   alfa=2*math.asin(sa2)
   area=alfa/2*R*R
   area-=R**2/2*math.sin(alfa)
   area+=(dv-dh)*(h-v)/2
   return area

def areacoord(d1,d2,R):
   d1=min(d1,R)
   cosa1=d1/R
   a1=2*math.acos(cosa1)
   ar1=R**2/2*(a1-math.sin(a1))
   d2=min(d2,R)
   cosa2=d2/R
   a2=2*math.acos(cosa2)
   ar2=R**2/2*(a2-math.sin(a2))
   return ar1-ar2
   
def areainter(d1,d2,v1,v2,R):
   d1=min(d1,R)
   d2=min(d2,R)
   h1=(R**2-d1**2)**0.5
   h2=(R**2-d2**2)**0.5
   v1=min(h1,v1)
   v2=min(h1,v2)
   a1=areac(h1,max(v1,h2),d1,R)      
   a2=areac(h1,max(v2,h2),d1,R)
   if v1<h2:
      a1+=(h2-v1)*(d2-d1)
   if v2<h2:
      a2+=(h2-v2)*(d2-d1)
   return a1-a2

def probability(vals):
   f, R, t, r, g = vals
   PT=math.pi*(R**2)
   PC=(math.pi*(R**2-(R-t-f)**2))/PT
   rr=r+min(f,g/2)
   gg=g-2*min(f,g/2)
   d=r+min(g/2,f)
   PVH=0
   PV=areacoord(0,d,R-t-f)
   #interrsection
   v=r+min(g/2,f)
   PVH += areainter(0,d,0,v,R-t-f)
   for j in xrange(10000000):
      v+=gg
      if v>R-t-f:
         break
      PVH += areainter(0,d,v,v+2*rr,R-t-f)
      v+=2*rr
   #end intersection
   for i in xrange(10000000):
      d+=gg
      if d>R-t-f:
         break
      PV+=areacoord(d,d+2*rr,R-t-f)
      #interrsection
      v=r+min(g/2,f)
      #print "-",areainter(d,d+2*rr,0,v,R-t-f)
      PVH += areainter(d,d+2*rr,0,v,R-t-f)
      for j in xrange(10000000):
         v+=gg
         if v>R-t-f:
            break
         PVH += areainter(d,d+2*rr,v,v+2*rr,R-t-f)
         v+=2*rr
      #end intersection
      d+=2*rr
   PV=2*PV/PT
   PVH=4*PVH/PT
   #print areac(R-t-f,0,0,R-t-f)*4,math.pi*((R-t-f)**2)
   #PV=2*(areacoord(0,R-t-f,R-t-f))/PT
   return PC + 2*PV - PVH

if __name__ == "__main__":
   import sys
   N = int(sys.stdin.readline())   
   for i in xrange(N):
      vals=sys.stdin.readline().strip().split(" ")
      vals=map(float,vals)
      print "Case #%d: %.6f" %(i+1,probability(vals))
