#include<cstdio>
#include<vector>
#include<algorithm>
//                         Last Change:  2011-06-04 23:03:09
using namespace std;
struct inter
{
	int x,y,v;
	bool operator <(const inter &a)const
	{
		return x<a.x;
	}
}e[3001];
bool cmp(const inter &x,const inter &y)
{
	return x.v<y.v;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int _,x,s,r,t,n;
	int cas=0;
	for(scanf("%d",&_);_--;)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		for(int i=1;i<=n;++i)
			scanf("%d%d%d",&e[i].x,&e[i].y,&e[i].v);
		sort(e+1,e+n+1);
		e[++n].x=x,e[n].y=x;
		int nn=n;
		for(int i=0;i<n;++i)
			if(e[i].y!=e[i+1].x)
			{
				e[++nn].x=e[i].y;
				e[nn].y=e[i+1].x;
				e[nn].v=-s;
			}
		sort(e+1,e+nn+1);
		--nn;
		double time=0;
		for(int i=1;i<=nn;++i)
			time+=double(e[i].y-e[i].x)/(e[i].v<0?s:e[i].v+s);
		sort(e+1,e+nn+1,cmp);
		double rt=t;
		for(int i=1;i<=nn&&rt>0;++i)
		{
			double tt=double(e[i].y-e[i].x)/(e[i].v<0?r:r+e[i].v);
			if(rt>=tt)
			{
				time-=double(e[i].y-e[i].x)/(e[i].v<0?s:e[i].v+s);
				time+=tt;
				rt-=tt;
			}
			else
			{
				time-=double(e[i].y-e[i].x)/(e[i].v<0?s:e[i].v+s);
				double d=(e[i].v<0?r:r+e[i].v)*rt;
				time+=rt+(e[i].y-e[i].x-d)/(e[i].v<0?s:e[i].v+s);
				rt=0;
			}
		}
		printf("Case #%d: %.10f\n",++cas,time);
	}
	return 0;
}
