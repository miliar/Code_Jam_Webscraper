import sys
import math
def sqr(a,b,c):
    return a*a+b*b+c*c
def solve(a,b,c):
    delta=b*b-4*a*c
    if(delta<0):
        return 0
    f=(-b+math.sqrt(delta))/(2*a)
    s=(-b-math.sqrt(delta))/(2*a)
    if(f<0):
        if(s<0):
            return 0
        else:
            return s
    else:
        if(s<0):
            return f
        else:
            return min(f,s)

sys.stdin = open('i.in')
output = open('o.txt', mode='w')
n=int(input())
for i in range(n):
    x,y,z=[0,0,0]
    vx,vy,vz=[0,0,0]
    k=int(input())
    for j in range(k):
        tx,ty,tz,tvx,tvy,tvz = [int(l) for l in input().split()]
        x+=tx
        vx+=tvx
        y+=ty
        vy+=tvy
        z+=tz
        vz+=tvz
    a=sqr(vx,vy,vz)
    b=2*(x*vx+y*vy+z*vz)
    c=sqr(x,y,z)
    if(a==0):
        if(b*c<0):
            tmin=-c/b
        else:
            tmin=0
    else:
        if(b*a>0):
            tmin=solve(a,b,c)
        else:
            tmin=-b/(2*a)
    if(a==0 and b==0):
        tmin=0
        inter=c
    else:
        inter=a*tmin*tmin+b*tmin+c
        if(inter<0):
            inter=0
    dmin=math.sqrt(inter)/k
    print('Case #%d: %.8f %.8f' %(i+1,dmin,tmin),file=output)
    
        
    
    
