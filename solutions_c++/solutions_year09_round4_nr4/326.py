#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+0.0);
}

double min(double a,double b) { return a<b?a:b; };
double max(double a,double b) { return a>b?a:b; };

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int n,i,j;
		int x[10],y[10],r[10];
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d%d%d",&x[i],&y[i],&r[i]);
		if (n==1) printf("%d\n",r[0]);
		if (n==2) printf("%d\n",max(r[0],r[1]));
		if (n==3)
		{
			double ans=1e10,z;

			z=dist(x[0],y[0],x[1],y[1]);
			z=max(r[2],(z+r[0]+r[1])*0.5);
			ans=min(z,ans);

			z=dist(x[0],y[0],x[2],y[2]);
			z=max(r[1],(z+r[0]+r[2])*0.5);
			ans=min(z,ans);

			z=dist(x[2],y[2],x[1],y[1]);
			z=max(r[0],(z+r[2]+r[1])*0.5);
			ans=min(z,ans);

			printf("%lf\n",ans);
		}
	}

	return 0;
}