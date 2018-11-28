#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
const double eps = 1e-8;
struct Node
{
	int p,v;
}point[205];
int d,n;
double max1(double a,double b)
{
	return a>b?a:b;
}
bool solve(double t)
{
	int i;
	double pol[205],por[205];
	pol[0] = point[0].p - t;
	por[0] = pol[0] + (point[0].v - 1) * d;
	if(fabs(por[0] - point[0].p) > t + eps)
		return false;
	for( i = 1 ; i < n ; i ++)
	{
		pol[i] = max1(por[i-1]+d,point[i].p - t);
		por[i] = pol[i] + (point[i].v - 1) * d;
		if(fabs(pol[i] - point[i].p) > t +eps|| fabs(por[i]-point[i].p) > t+eps)
			return false;
	}
	return true;
}
int main()
{	freopen("B-small-attempt2.in","r",stdin);	freopen("B-small-attempt2.out","w",stdout);
	int t;
	int g = 1;
	scanf("%d",&t);
	while(t--)
	{
		
		int i;
		scanf("%d%d",&n,&d);
		for( i = 0 ; i < n ; i ++)
			scanf("%d%d",&point[i].p,&point[i].v);
		double left = 0;
		double right = 1000000000;
		solve(0);
		while(left + eps <
			right )
		{
			double mid = (left + right)/2;
			if(solve(mid))
				right = mid;
			else
				left = mid;
		}
		printf("Case #%d: ",g++);
		printf("%.12lf\n",left);


	}
	return 0;
}