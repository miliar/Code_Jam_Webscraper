#include "stdio.h"
#include "math.h"
int main()
{
	double x[3],y[3],r[3],res,s;
	int kase,t,n;
	scanf("%d",&kase);
	for(t=1;t<=kase;t++)
	{
		scanf("%d",&n);
		if(n==1)
		{
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			printf("Case #%d: %lf\n",t,r[0]);
		}
		else if(n==2)
		{
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			scanf("%lf%lf%lf",&x[1],&y[1],&r[1]);
			if(r[0]>r[1])
				printf("Case #%d: %lf\n",t,r[0]);
			else
				printf("Case #%d: %lf\n",t,r[1]);
		}
		else
		{
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			scanf("%lf%lf%lf",&x[1],&y[1],&r[1]);
			scanf("%lf%lf%lf",&x[2],&y[2],&r[2]);
			res=1000000.0;
			s=sqrt( (x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]) )+r[0]+r[1];
			if(r[2]>s)s=r[2];
			if(res>s) res=s;
			s=sqrt( (x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]) )+r[0]+r[2];
			if(r[1]>s)s=r[1];
			if(res>s) res=s;
			s=sqrt( (x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]) )+r[2]+r[1];
			if(r[0]>s)s=r[0];
			if(res>s) res=s;
			printf("Case #%d: %lf\n",t,res/2.0);
		}
	}
	return 0;
}