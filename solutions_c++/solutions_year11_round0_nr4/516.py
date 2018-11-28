#include <iostream>
#include <cstdio>
using namespace std;
int p[1001];
bool vis[1001];
int main()
{
	int i,cas = 1,n,r,cnt,ans,t,res;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		memset(vis,0,sizeof(vis));
		ans = 0;
		res = 0;
		for (i = 1;i <= n;i++)
		{
			scanf("%d",&p[i]);
			if (p[i] == i)
				res++;
		}
		for (i = 1;i <= n;i++)
		{
			if (!vis[i])
			{
				r = i;
				cnt = 1;
				while (p[r] != i)
				{
					r = p[r];
					vis[r] = true;
					cnt++;
				}
				ans += cnt;
			}
		}
		ans -= res;
		printf("Case #%d: %d.000000\n",cas++,ans);
	}
	return 0;
}