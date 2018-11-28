#include <stdio.h>
#include <math.h>
  int main()
	{
	long T,I,i,x,y,z,vx,vy,vz,n;
	double sx,sy,sz,svx,svy,svz,a,b,c,d,t;
	scanf("%ld",&T);
	for(I=1;I<=T;I++)
	  {
	  scanf("%ld",&n);
	  sx=sy=sz=svx=svy=svz=0;
	  for(i=0;i<n;i++)
		{
		scanf("%ld%ld%ld%ld%ld%ld",&x,&y,&z,&vx,&vy,&vz);
		sx+=x;
		sy+=y;
		sz+=z;
		svx+=vx;
		svy+=vy;
		svz+=vz;
		}
	  a=svx*svx+svy*svy+svz*svz;
	  b=2*(sx*svx+sy*svy+sz*svz);
	  c=sx*sx+sy*sy+sz*sz;
	  d=b*b-4*a*c;
	  if(a==0) t=0;
		  else if(d<0) {
					   t=-b/(2*a);
					   if(t<0) t=0;
					   }
				  else {
					   t=0;
					   if((-b-sqrt(d))/(2*a)>0) t=(-b-sqrt(d))/(2*a);
					   if((t>(sqrt(d)-b)/(2*a))&&((sqrt(d)-b)/(2*a)>0)) t=(sqrt(d)-b)/(2*a);
					   }
	  d=sqrt((sx+svx*t)*(sx+svx*t)+(sy+svy*t)*(sy+svy*t)+(sz+svz*t)*(sz+svz*t))/n;
	  printf("Case #%ld: %.8lf %.8lf\n",I,d,t);
	  }
	}
