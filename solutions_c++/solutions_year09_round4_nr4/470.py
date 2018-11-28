#include<iostream>
#include<cmath>
using namespace std;
struct point
{
	double x,y;
}cen[4];

double r[4];

double dist(int i,int j)
{
	int dx=cen[i].x-cen[j].x;
	int dy=cen[i].y-cen[j].y;
	return sqrt(dx*dx+dy*dy);
}

int main()
{
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%lf%lf%lf",&cen[i].x,&cen[i].y,&r[i]);
		printf("Case #%d: ",t);
		if(n==1)
		{
			printf("%.10lf\n",r[0]);
			continue;
		}
		if(n==2)
		{
			printf("%.10lf\n",max(r[0],r[1]));
			continue;
		}
		if(n==3)
		{
			double ans1=max((dist(0,1)+r[0]+r[1])/2.0,r[2]);
			double ans2=max((dist(1,2)+r[1]+r[2])/2.0,r[0]);
			double ans3=max((dist(0,2)+r[0]+r[2])/2.0,r[1]);
			printf("%.10lf\n",min(min(ans1,ans2),ans3));
			continue;
		}
	}
	return 0;
}
