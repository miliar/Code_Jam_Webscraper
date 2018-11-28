#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 1000030

int d,c,n;
int p[M];

bool solve(double x)
{
	int i;
	double pos=p[0]-x,y;
	for(i=1;i<n;i++)
	{
		y=pos+d;
		if(y>p[i])
		{
			if(p[i]+x<y)
				return 0;
			pos=y;
		}
		else
		{
			if(p[i]-x<y)
				pos=y;
			else
				pos=p[i]-x;
		}
	}
	return 1;
}

int main()
{
	int i,j,k,t,tc=1;
	int pp,v;
	double low,mid,high;
	freopen("gcj/2011.5.22/B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&c,&d);
		n=0;
		for(i=0;i<c;i++)
		{
			scanf("%d%d",&pp,&v);
			for(j=0;j<v;j++)
			{
				p[n]=pp;
				n++;
			}
		}
		sort(p,p+n);
		low=0;
		high=d;
		high*=n;
		while(low<high-0.00000001)
		{
			mid=(high+low)/2;
			if(solve(mid))
			{
				high=mid;
			}
			else
				low=mid;
		}
		printf("Case #%d: ",tc++);
		if(solve(low))
			printf("%.7lf\n",low);
		else
			printf("%.7lf\n",high);
	}
	return 0;
}
/*
3
1 100 50
10 10 100
9 80 56
*/

