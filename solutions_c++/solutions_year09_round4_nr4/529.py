#include <stdio.h>
#include <math.h>

double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	int c;
	scanf("%d",&c);
	int ci;
	double x[3],y[3],r[3];
	for (ci=0;ci<c;ci++)
	{
		int n;
		scanf("%d",&n);
		int ni;
		for (ni=0;ni<n;ni++)
			scanf("%lf %lf %lf",&x[ni],&y[ni],&r[ni]);
		if (n==1)
		{
			printf("Case #%d: %lf\n",ci+1,r[0]);
			continue;
		}
		if (n==2)
		{
			printf("Case #%d: %lf\n",ci+1,(r[0]>r[1])?r[0]:r[1]);
			continue;
		}
		double rb0,rb1,rb2;
		rb0=(dist(x[1],y[1],x[2],y[2])+r[1]+r[2])/2;
		rb1=(dist(x[2],y[2],x[0],y[0])+r[2]+r[0])/2;
		rb2=(dist(x[0],y[0],x[1],y[1])+r[0]+r[1])/2;
		double r0,r1,r2;
		r0=(rb0>r[0])?rb0:r[0];
		r1=(rb1>r[1])?rb1:r[1];
		r2=(rb2>r[2])?rb2:r[2];
		double min=r0;
		if (r1<min) min=r1;
		if (r2<min) min=r2;
		printf("Case #%d: %lf\n",ci+1,min);
	}
	return 0;
}
