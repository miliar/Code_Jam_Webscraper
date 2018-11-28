#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
struct P
{
	double b,e,w;
	double len;
}p[1000010];
bool cmp(P a,P b)
{
	return a.w<b.w;
}
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		double x,s,r,t;
		int n;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		int i;
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&p[i].b,&p[i].e,&p[i].w);
		}
		sort(p,p+n,cmp);		
		double ans=0;
		printf("Case #%d: ",_);
		double res=x;
		for(i=0;i<n;i++)
		{
			res=res-(p[i].e-p[i].b);
		}
		if(t!=0)
		{
			if(res/r<=t)
			{
				ans+=(res)/r;
				t-=(res)/r;
			}
			else
			{
				ans+=t;
				ans+=(res-t*(r))/(s);
				t=0;
			}
		}
		else
		{
			ans+=(res)/(s);
		}
		for(i=0;i<n;i++)
		{
			if(t!=0)
			{
				if((p[i].e-p[i].b)/(p[i].w+r)<=t)
				{
					ans+=(p[i].e-p[i].b)/(p[i].w+r);
					t-=(p[i].e-p[i].b)/(p[i].w+r);
				}
				else
				{
					ans+=t;
					ans+=(p[i].e-p[i].b-t*(r+p[i].w))/(s+p[i].w);
					t=0;
				}
			}
			else
			{
				ans+=(p[i].e-p[i].b)/(s+p[i].w);
			}
		}
		printf("%0.8lf\n",ans);
	}
	return 0;
}