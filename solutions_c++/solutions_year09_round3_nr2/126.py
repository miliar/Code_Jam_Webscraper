#include <stdio.h>
#include <math.h>
double x[2],y[2],z[2];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	for (int k=1;k<=cases;k++)
	{
		x[0]=x[1]=y[0]=y[1]=z[0]=z[1]=0;
		int n;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			int t1,t2,t3,t4,t5,t6;
			scanf("%d%d%d%d%d%d",&t1,&t2,&t3,&t4,&t5,&t6);
			x[0]+=t1;x[1]+=t4;
			y[0]+=t2;y[1]+=t5;
			z[0]+=t3;z[1]+=t6;
		}
		x[0]/=n,x[1]/=n,y[0]/=n,y[1]/=n,z[0]/=n,z[1]/=n;
		double a=x[1]*x[1]+y[1]*y[1]+z[1]*z[1],b=2*(x[0]*x[1]+y[0]*y[1]+z[0]*z[1]),c=x[0]*x[0]+y[0]*y[0]+z[0]*z[0];
		double tmin=-b/(2*a);
		if (a<1e-8 || tmin<0) tmin=0;
		if (tmin<1e-5) tmin=0;
		double dmin=a*tmin*tmin+b*tmin+c;
		if (dmin<1e-6) dmin=0;
		printf("Case #%d: %f %f\n",k,sqrt(dmin),tmin);
	}
	return 0;
}