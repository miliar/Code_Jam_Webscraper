#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
struct node
{
	double x,y,r;
}p[50];

int cs,n;
int cn = 1;

double dist(node a,node b)
{
	return sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
}

double max(double a,double b)
{
	return a>b?a:b;
}

double min(double a,double b)
{
	return a<b?a:b;
}

int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("d.txt","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
		if(n == 1)
		{
			printf("Case #%d: %.6lf\n",cn++,p[0].r);
		}
		else if(n == 2)
		{
			double ans = p[0].r;
			ans = max(p[0].r,p[1].r);
			printf("Case #%d: %.6lf\n",cn++,ans);
		}
		else if(n == 3)
		{
			double a1 = max(p[2].r,(dist(p[0],p[1])+(p[0].r+p[1].r))/2);
			double a2 = max(p[1].r,(dist(p[0],p[2])+(p[0].r+p[2].r))/2);
			double a3 = max(p[0].r,(dist(p[2],p[1])+(p[2].r+p[1].r))/2);
			double ans = a1;
			ans = min(ans,a2);
			ans = min(ans,a3);
			printf("Case #%d: %.6lf\n",cn++,ans);
		}
	}
	return 0;
}

