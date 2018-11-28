#include <cstdio>
#include <cstring>
#include <cmath>

double max(double a,double b)
{
	return a>b?a:b;
}

double min(double a,double b)
{
	return a<b?a:b;
}

struct Point
{
	double x,y;
}p[3];

double r[3];

double dis(Point &a,Point &b)
{
	double dx=a.x-b.x,dy=a.y-b.y;
	return sqrt(dx*dx+dy*dy);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	int n,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf",&p[i].x,&p[i].y,&r[i]);
		printf("Case #%d: ",ca++);
		if(n==1) printf("%lf\n",r[0]);
		else if(n==2) printf("%lf\n",max(r[0],r[1]));
		else
		{
			double ans=1e20;
			ans=min(ans,max(2*r[0],dis(p[1],p[2])+r[1]+r[2]));
			ans=min(ans,max(2*r[1],dis(p[0],p[2])+r[0]+r[2]));
			ans=min(ans,max(2*r[2],dis(p[0],p[1])+r[0]+r[1]));
			printf("%lf\n",ans/2.0);
		}
	}
	return 0;
}