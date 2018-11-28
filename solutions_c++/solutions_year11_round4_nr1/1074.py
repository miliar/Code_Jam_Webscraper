#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
struct point
{
	int x,y;
	point(){}
	point(int x,int y)
	{
		this->x = x;
		this->y = y;
	}
}p[1005];
bool cmp(point a,point b)
{
	return a.y < b.y;
}
int main()
{  freopen("A-large(1).in","r",stdin);	
	freopen("A-large(1).out","w",stdout);
	int f;
	int g = 1;
	scanf("%d",&f);
	while(f--)
	{
		int n;
		double x,s,r;
		double t;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		int i;
		for( i = 0 ; i < n; i ++)
		{
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			p[i] = point(b-a,c);
			x-= (b-a);
		}
		p[i] = point(x,0);
		double ans = 0;
		sort(p,p+n+1,cmp);
		for( i = 0 ; i <= n ; i ++)
		{
			double q = p[i].x / (p[i].y + r);
			if(q<=t)
			{
				ans += q;
				t-= q;
			}
			else
			{
				ans += t + ((double)p[i].x - t * (p[i].y + r))/(p[i].y+s);
				t = 0;
			}
		}
		printf("Case #%d: %.12lf\n",g++,ans);
		
	}
	return 0;
}