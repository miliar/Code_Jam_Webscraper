#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define eps 1e-10
#define print(x) cout<<#x<<":"<<x<<"\n"
#define dist(x1,y1,x2,y2) sqrt(((x1)-(x2))*((x1)-(x2))+((y1)-(y2))*((y1)-(y2)))
#define pi acos(-1)
#define cross(x1,y1,x2,y2) (x1*y2-x2*y1)

int cs,c,x,i,j;
double f,R,t,r,g,r2,area,s;

double section(double h,double v)
{
  double area,h2,v2,theta;

  h2=sqrt(r2*r2-h*h);
  v2=sqrt(r2*r2-v*v);
  theta=atan(v2/v)-atan(h/h2);
  area=pi*r2*r2*theta/(2*pi);
  area-=fabs(cross(h2,h,v,h)/2)+fabs(cross(v,v2,v,h)/2);
  return area;
}
double intersection(double x,double y)
{
  double area;

  if(dist(0,0,x,y+s)<r2+eps)
    if(dist(0,0,x+s,y)<r2+eps)
	{  
	  area=section(y,x)-section(y,x+s)-section(y+s,x);
	}
    else
	  area=section(y,x)-section(y+s,x);
  else
    if(dist(0,0,x+s,y)<r2+eps)
	  area=section(y,x)-section(y,x+s);
    else
	{
	  area=section(y,x);
    }
  return area;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
	x=0;
	r2=R-t-f;
	while(r+x*(g+2*r)<r2+eps)
	  x++;
	area=0;
	if(r2>-eps && (g-2*f)>-eps)
	{
	  s=(g-2*f);
	  for(i=0;i<x;i++)
	    for(j=0;j<x;j++)
	      if(dist(0,0,r+i*(g+2*r)+f,r+j*(g+2*r)+f)<r2+eps)
		    if(dist(0,0,r+i*(g+2*r)+f+s,r+j*(g+2*r)+f+s)<r2+eps)
			{
		      area+=s*s;
		    }
			else
			{
		      area+=intersection(r+i*(g+2*r)+f,r+j*(g+2*r)+f);
			}
	  area*=4;
	}
    printf("Case #%d: %.6lf\n",c+1,1-area/(pi*R*R));
  }
  return 0;
}
