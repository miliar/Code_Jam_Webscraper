#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

struct Point{
	int s,e,v;
};
Point a[1001];
int speed[201];
int cmp(const void *a,const void *b)
{
	return ((Point *)a)->s-((Point *)b)->s;
}
int main()
{
	int repeat,ri=1,i;
	int x,s,r,t,n;
	int sum;
	double result,left;

	freopen("A-large (1).in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&repeat);
	while(repeat--)
	{
		memset(speed,0,sizeof(speed));
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		result=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&a[i].s,&a[i].e,&a[i].v);
			x-=a[i].e-a[i].s;
			speed[a[i].v]+=a[i].e-a[i].s;
		}
		if( t<=1.0*x/r)
		{
			result=1.0*(x-t*r)/s+t;
			left=0;
		}
		else
		{
			result=1.0*x/r;
			left=t-1.0*x/r;
		}
		for(i=0;i<=200;i++)
		{
			if( speed[i]==0) continue;
			else
			{
				if( left==0)
					result+=1.0*speed[i]/(s+i);
				else if( left<=1.0*speed[i]/(i+r) )
				{
					result+=1.0*(speed[i]-left*(i+r))/(s+i)+left;
					left=0;
				}
				else
				{
					result+=1.0*speed[i]/(i+r);
					left-=1.0*speed[i]/(i+r);
				}
			}
		}
		printf("Case #%d: %.12f\n",ri++,result);
	}
	return 0;
}
