#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;

#define N 1000

int a[N+100];
bool vis[N+100];
int p[N+100];

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int i,j,t,n;
	i64 sum;
	double res;
	double s;
	scanf("%d",&t);
	int l;
	int first,cur;
	p[0]=0;
	p[1]=0;
	for (i=2;i<=N;i++)
		p[i]=i;
	for (int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		memset(vis,false,sizeof(vis));
		res=0;
		for (i=1;i<=n;i++)
			if (!vis[i])
			{
				l=1;
				first=i;
				cur=i;
				vis[i]=true;
				while (first!=a[cur])
				{
					cur=a[cur];
					vis[cur]=true;
					l++;
				}
				res+=p[l];
			}
			printf("Case #%d: %llf\n",cnt,res);
	}
	return 0;
}