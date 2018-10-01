import sys
from math import sqrt
from math import pi
from math import acos
N=int(input())
def inside(i,j,R,t,r,g):
  ins = [False,False,False,False]
  for x in range(2):
    for y in range(2):
      ins[x+2*y] = ((r+i*(g+2*r)+x*g)**2 + (r+j*(g+2*r)+y*g)**2 <= (R-t)**2)
  return ins

def area(a,b,y,rho):

  alpha=acos(a/float(rho))
  beta=acos(b/float(rho))
  s = 0.5*((alpha-beta)*rho**2-a*sqrt(rho**2-a**2)+b*sqrt(rho**2-b**2))

  return s-(b-a)*y

for step in range(N):
  sys.stderr.write(str(step+1)+' ')
  f, R, t, r, g = map(float,raw_input().split())
  if 2*f>=g or f+t>=R:
    prob=1.0
  else:
    g -= 2*f
    r += f
    t += f

    BL=0
    BR=1
    UL=2
    UR=3

    S=0
    i=0
    while True:
      
      x=r+i*(g+2*r)

      if not x<=R-t:
        break
      xmin=x
      xmax=x+g

      if xmax<=R-t:
        Y = sqrt((R-t)**2-xmax**2)
        if Y>g+r:
          j=1+int((Y-g-r)/float(g+2*r))
        else:
          j=0
      else:
        j=0
      
      S+=j*g**2

      while True:



        ins=inside(i,j,R,t,r,g)


        if not ins[BL]:

          break
        if ins[BL]:
          y=r+j*(g+2*r)

          xmin=x
          xmax=x+g
          if ins[UL]:

            xmin=sqrt((R-t)**2-(y+g)**2)

          if not ins[BR]:
            xmax=sqrt((R-t)**2-y**2)



          value = area(xmin,xmax,y,R-t)+(xmin-x)*g

          S += value

        j+=1
      i+=1
    prob=1-S/(0.25*pi*R**2)


  print 'Case #%s: %.6f'%(step+1,prob)
  
sys.stderr.write('\n')
