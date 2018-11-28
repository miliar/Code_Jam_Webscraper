#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
struct E
{
	double r;
	int id;
}tt[1010];
double ans[1010][2];
bool cmp(E a,E b)
{
	return a.r>b.r;
}
int main(void)
{
	int T,n,W,L;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	int g=0;
	while(T--)
	{
		scanf("%d%d%d",&n,&W,&L);
		for(int i=1;i<=n;i++)
		{
			scanf("%lf",&tt[i].r);
			tt[i].id=i;			
		}
		sort(tt+1,tt+1+n,cmp);
		ans[tt[1].id][0]=0.0;
		ans[tt[1].id][1]=0.0;
		double low=0.0;
		int mark=1;
		for(int i=2;i<=n;i++)
		{
			if(tt[i].r*2+ans[tt[i-1].id][0]+tt[i-1].r<=W)
			{
				ans[tt[i].id][0]=ans[tt[i-1].id][0]+tt[i-1].r+tt[i].r;
				ans[tt[i].id][1]=low;
			}
			else
			{
				ans[tt[i].id][0]=0.0;
				ans[tt[i].id][1]=low+tt[i].r+tt[mark].r;
				low=low+tt[i].r+tt[mark].r;
				mark=i;
			}
		}
		printf("Case #%d:",++g);
		for(int i=1;i<=n;i++)
		{
			printf(" %lf %lf",ans[i][0],ans[i][1]);
		}
		printf("\n");  
						
	}
	return 0;
}
