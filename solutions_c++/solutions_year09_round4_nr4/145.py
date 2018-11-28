#include <iostream>
#include <cmath>

#define sqr(x) (x)*(x)

using namespace std;

struct Tcircle{
	double x, y, r;
};
Tcircle a[10];
int n;

void init()
{
	cin>>n;
	for (int i=0;i<n;i++)
		cin>>a[i].x>>a[i].y>>a[i].r;
}
double rad(Tcircle &a, Tcircle &b)
{
	return (a.r+b.r+sqrt(sqr(a.x-b.x)+sqr(a.y-b.y)+0.0))/2.0;
}
double calc()
{	
	double ans=1e6;
	if (n==1) return a[0].r;
	else if (n==2) return max(a[0].r, a[1].r);
	
	double r;
	for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++)
			for (int k=0;k<n;k++)
				if (k!=i && k!=j)
				{
					ans = min(ans,max((double)a[k].r, rad(a[i],a[j])));					
				}
	return ans;
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		printf("Case #%d: %.6lf\n",i+1,calc());		
	}
}
