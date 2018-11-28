#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int ms[510][510];
int n,m;
void init()
{
	int d;
	scanf("%d%d%d",&n,&m,&d);
	for(int i=0;i<n;i++)
	{
		char str[1024];
		scanf("%s",str);
		for(int j=0;j<m;j++)
			ms[i][j]=(str[j]-'0')+d;
	}
}
int solve()
{
	for(int k=min(m,n);k>=3;k--)
	{
		for(int i=k;i<=n;i++)
			for(int j=k;j<=m;j++)
			{
				double sx=0,sy=0;
				double cx=(j-k+j-1)*0.5;
				double cy=(i-k+i-1)*0.5;
				for(int y=i-k;y<i;y++)
					for(int x=j-k;x<j;x++)
					{
						if(y==i-k&&x==j-k) continue;
						if(y==i-k&&x==j-1) continue;
						if(y==i-1&&x==j-k) continue;
						if(y==i-1&&x==j-1) continue;
						sx+=(x-cx)*ms[y][x];
						sy+=(y-cy)*ms[y][x];
					}
				if(fabs(sx)<1e-6&&fabs(sy)<1e-6) return k;
			}
	}
	return -1;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		init();
		printf("Case #%d: ",cs);
		int ans=solve();
		if(ans<3) puts("IMPOSSIBLE"); else printf("%d\n",ans);
	}
	return 0;
}
