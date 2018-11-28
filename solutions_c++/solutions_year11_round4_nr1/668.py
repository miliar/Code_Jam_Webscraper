#include<algorithm>
#include<cstdio>
using namespace std;

const int mx=1010;

int X,S,R,t,n;
struct be
{
	int s,t;
	double dis;
	int w;
}e[mx];

bool cmp(be a,be b)
{
	return a.w<b.w;
}

int main()
{
	int i;
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&n);
		int zero=X;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&e[i].s,&e[i].t,&e[i].w);
			e[i].dis=e[i].t-e[i].s;
			zero-=e[i].t-e[i].s;
		}
		e[n].s=0;
		e[n].t=zero;
		e[n].w=0;
		e[n].dis=zero;
		double ans=0;
		sort(e,e+n+1,cmp);
		double left=t;
		for(i=0;i<=n;i++)
		{
			double need_t=e[i].dis/(R+e[i].w);
			if(left>=need_t)
			{
				left-=need_t;
				ans+=need_t;
			}
			else
			{
				double dis=e[i].dis;
				dis-=left*(R+e[i].w);
				ans+=left;
				left=0.0;
				ans+=dis/(S+e[i].w);
			}
		}
		printf("Case #%d: %.12lf\n",ca++,ans);
	}
	return 0;
}
