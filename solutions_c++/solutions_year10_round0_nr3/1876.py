#include <stdio.h>

const int T = 50;
const int R = 100000000;
const int K = 1000000000;
const int N = 1000;
const int G = 10000000;

main()
{
	int t, r, k, n;
	int g[N], get[N], next[N];
	int now;
	long long ans;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (int j=0;j<n;j++)
			scanf("%d", &g[j]);
		
		ans=0;
		for (int j=0;j<n;j++)
		{
			now=j;
			get[j]=0;
			while (get[j]+g[now]<=k && (now!=j||get[j]==0))
			{
				get[j]+=g[now];
				now=(now+1)%n;
			}
			next[j]=now;
		}
		
		now=0;
		for (int j=0;j<r;j++)
		{
			ans+=get[now];
			now=next[now];
		}
		
		printf("Case #%d: %lld\n", i, ans);
	}
}
