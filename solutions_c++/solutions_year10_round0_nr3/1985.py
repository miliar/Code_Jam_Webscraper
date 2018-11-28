#include <stdio.h>
#include <string.h>
const int MAXN = 1001;
long long arr[MAXN];
long long sum[MAXN];
int len[MAXN];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d",&T);
	for (int t=0;t<T;t++)
	{
		int n,r;
		long long k;
		scanf("%d%I64d%d",&r,&k,&n);
		for (int i=0;i<n;i++)
			scanf("%I64d",&arr[i]);
		memset(sum,0,sizeof(sum));
		memset(len,0,sizeof(len));
		for (int i=0;i<n;i++)
		{
			while (sum[i]+arr[(i+len[i])%n]<=k && len[i]<n)
			{
				sum[i]+=arr[(i+len[i])%n];
				len[i]++;
			}
		}
		long long ans = 0;
		int s=0;
		for (int i=0;i<r;i++)
		{
			ans+=sum[s];
			s+=len[s];
			if (s>=n)
				s-=n;
		}
		printf("Case #%d: %I64d\n",t+1,ans);
	}
	return 0;
}
