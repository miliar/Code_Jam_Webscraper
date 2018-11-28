#include <stdio.h>
#include <math.h>
#define y1 yy1

int T,t,x,y,r,x1,y1,r1,x2,y2,r2,n;
double z,u,v;

double d(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++t);
		scanf("%d",&n);
		if(n==1)
		{
			scanf("%d%d%d",&x,&y,&r);
			printf("%d\n",r);
			continue;
		}
		if(n==2)
		{
			scanf("%d%d%d%d%d%d",&x1,&y1,&r1,&x2,&y2,&r2);
			if(r1<r2)
				r1=r2;
			printf("%d\n",r2);
			continue;
		}
		scanf("%d%d%d%d%d%d%d%d%d",&x,&y,&r,&x1,&y1,&r1,&x2,&y2,&r2);
		z=d(x1,y1,x2,y2)+r1+r2;
		if(z<2*r)
			z=2*r;
		u=d(x,y,x2,y2)+r+r2;
		if(u<2*r1)
			u=2*r1;
		v=d(x1,y1,x,y)+r1+r;
		if(v<2*r2)
			v=2*r2;
		if(z>u)
			z=u;
		if(z>v)
			z=v;
		printf("%lf\n",z/2.0);
	}
	return 0;
}



