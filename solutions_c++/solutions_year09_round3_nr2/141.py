#include<iostream>
#include<stdio.h>
#include<string.h>
#include<cmath>
using namespace std;
double x1,x2,y11,y2,z1,z2,x3,z3,y3,x4,y4,z4,at,ad,af;
double dx[1010],dy[1010],dz[1010],fx[1010],fy[1010],fz[1010];
double pf(double a)
{
	return a*a;
}
int main()
{
	int i,j,k,l,n,z,y;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&z);
	for(y=1;y<=z;y++)
	{
		scanf("%d",&n);
		x3=x4=z3=z4=y3=y4=0;
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf",dx+i,dy+i,dz+i,fx+i,fy+i,fz+i);
			x3+=dx[i];x4+=fx[i];
			y3+=dy[i],y4+=fy[i];
			z3+=dz[i],z4+=fz[i];
		}
		x3/=n;x4/=n;y3/=n;y4/=n;z3/=n;z4/=n;
		x4+=x3;
		y4+=y3;
		z4+=z3;

		ad=sqrt((pf((x4-x3)*(0-y3)-(y4-y3)*(0-x3))+pf((y4-y3)*(0-z3)-(z4-z3)*(0-y3))+pf((z4-z3)*(0-x3)-(x4-x3)*(0-z3)))/((x4-x3)*(x4-x3)+(y4-y3)*(y4-y3)+(z4-z3)*(z4-z3)));
		af=((x4-x3)*(0-x3)+(y4-y3)*(0-y3)+(z4-z3)*(0-z3))/((x4-x3)*(x4-x3)+(y4-y3)*(y4-y3)+(z4-z3)*(z4-z3));
		at=((x4-x3)*(x4-x3)+(y4-y3)*(y4-y3)+(z4-z3)*(z4-z3));
		if(at<=1e-9)
			af=-100;
		if(af<0)
		{
			af=0;
			ad=sqrt(pf(0-x3)+pf(0-y3)+pf(0-z3));
		}
		printf("Case #%d: %.8lf %.8lf\n",y,ad,af);
	}
	return 0;
}
