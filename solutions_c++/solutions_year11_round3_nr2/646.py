#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
long long cc[1000005],tl[1000005],sum[1000005];
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t1,q,l,n,c;
	long long t;
	scanf("%d",&t1);
	for (q = 1; q <= t1 ; q++)
	{
		scanf("%d%lld%d%d",&l,&t,&n,&c);
		for (int i = 0 ; i < c; i++)
			scanf("%lld",&cc[i]);
		memset(sum,0,sizeof(sum));
		for (int i = 1; i <= n; i++)
		{
			tl[i] = cc[(i-1) %c];
			sum[i] = sum[i-1] + 2 * tl[i];
		}
		long long delta = 0;
		long long ans = sum[n];
		if (l == 0) ; else
			if (l == 1)
			{
				for (int i = 1; i <= n; i++)
				{
					delta = 0;
					if (sum[i] >=t)
					{
						if (sum[i-1] >= t)
							delta = tl[i]; else
						{
							long long dist = (long long)((t - sum[i-1]) * 0.5);
							delta = tl[i] - dist;
						}
					}
					ans = min(ans,sum[n] - delta);
				}
			} else
			{
				for (int i = 1; i <= n; i++)
					for (int j = 1; j <= n; j++)
						if (i != j)
				{
					delta = 0;
					if (sum[i] >=t)
					{
						if (sum[i-1] >= t)
							delta = tl[i]; else
						{
							long long dist = (long long)((t - sum[i-1]) * 0.5);
							delta = tl[i] - dist;
						}
					}
					if (sum[j] >=t)
					{
						if (sum[j-1] >= t)
							delta += tl[j]; else
						{
							long long dist = (long long)((t - sum[j-1]) * 0.5);
							delta += tl[j] - dist;
						}
					}
					ans = min(ans,sum[n] - delta);
				}
			}
			printf("Case #%d: %lld\n",q,ans);
	}
	return 0;
}
