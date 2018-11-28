#include<stdio.h>
#include<algorithm>
using namespace std;

const int MAXN = 1000000;
const double eps = 1e-8;

double ans;
int lim,L,w,r,n;

struct pt
{
	int x,y,t;
}p[MAXN];
bool operator < (const pt &a,const pt &b)
{
	return a.t < b.t;
}
void calc(double dis,double speed)
{
	double tmp = dis / speed;
	if (ans + tmp < lim+eps)
		ans += tmp;
	else
	{		
		ans = lim + (dis - speed*(lim-ans)) / (speed-(r-w));
	}
}
int main()
{
	int test;
	
	
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		scanf("%d%d%d%d%d",&L,&w,&r,&lim,&n);
		for (int i=0;i<n;i++)
		{
			scanf("%d%d%d",&p[i].x,&p[i].y,&p[i].t);
			
		}
		int top = n;
		
		p[top].x = 0;
		p[top].y = p[0].x;
		p[top++].t = 0;
		
		for (int i=1;i<n;i++)
		{
			p[top].x = p[i-1].y;
			p[top].y = p[i].x;
			p[top++].t = 0;
		}
		p[top].x = p[n-1].y;
		p[top].y = L;
		p[top++].t = 0;	
		n = top;
		
		sort(p,p+n);
		double ans = 0;
		for (int i=0;i<n;i++)
		{
			//printf("p[%d] is %d %d %d\n",i,p[i].x,p[i].y,p[i].t);
			if (ans < lim)
			{
				double tmp = (double)(p[i].y - p[i].x) / (p[i].t + r);
				if (ans + tmp < lim+eps)
					ans += tmp;
				else
				{
					double dis = p[i].y - p[i].x; 
					ans = lim + (dis - (p[i].t + r)*(lim-ans)) / (p[i].t+w);
				}
			}
			else
				ans += (double)(p[i].y - p[i].x) / (p[i].t + w);
		}
		printf("Case #%d: %.8f\n",cas,ans);
	}
}

