#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <string>


#define M 1002

struct D{int s,e,w;
	bool friend operator < (const D &p,const D &q)
	{
		return p.w<q.w;
	}
}a[M];

int length,run,walk;
double b1,ans,max;

void process(int dist,int plus)
{
	b1=double(dist)/(run+plus);
	if(b1<=max) //full run
	{
		max-=b1;
		ans+=b1;
	}
	else
	{
		b1=(dist-max*(run+plus))/(walk+plus);
		ans+=max+b1;
		max=0;
	}
}

int main()
{
	int t,T=0,i,n;

	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d %d %d %lf %d",&length,&walk,&run,&max,&n);
		for(i=1;i<=n;++i) scanf("%d%d%d",&a[i].s,&a[i].e,&a[i].w);

		ans=0;
		for(i=1;i<=n;++i) process(a[i].s-a[i-1].e,0);
		process(length-a[n].e,0);
		std::sort(a+1,a+n+1);
		for(i=1;i<=n;++i) process(a[i].e-a[i].s,a[i].w);

		printf("Case #%d: %.12f\n",++T,ans);
	}
	return 0;
}
