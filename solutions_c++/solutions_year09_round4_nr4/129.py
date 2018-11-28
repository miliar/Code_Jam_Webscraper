#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

struct circle
{
	double x,y,r;
}c[20];
double sqr(double x){return x*x;}
double dis(circle a,circle b)
{
	return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}
double solve(int t,int s)
{
	return  (dis(c[t],c[s])+c[t].r+c[s].r)/2;
};
int T,i,j,k,n,m,I;
double ans;
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		scanf("%d",&n);
		for (i=0;i<n;++i)
			scanf("%lf%lf%lf",&c[i].x,&c[i].y,&c[i].r);
		if (n==1)
			ans=c[0].r;
		else if (n==2)
			ans=max(c[0].r,c[1].r);
		else if (n==3)
		{
			ans=max(solve(0,1),c[2].r);
			ans=min(ans,max(solve(1,2),c[0].r));
			ans=min(ans,max(solve(0,2),c[1].r));
		}
		printf("Case #%d: %.6lf\n",I,ans);
	}
	return 0;
}
