#include<stdio.h>

#define LL long long

int p[1000005];
int pr[80000];

int gene(int n)
{
	int i,j;
	for(i=2;i*i<=n;i++)
		if(!p[i])
			for(j = i*i ; j<=n ; j+=i)
				p[j] = 1;
//	cnt[1] = 0;
//	for(i=2;i<=n;i++)
//		cnt[i] = cnt[i-1] + (!p[i]);
	j = 0;
	for(i=2;i<=n;i++)
		if(!p[i])
			pr[j++] = i;
	return j;
}

int main()
{
	freopen("expen.in","r",stdin);
	freopen("expen.out","w",stdout);
	int m = gene(1000000);
	int i,t,cs = 0;
	LL n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld",&n);
		LL ans = 1;
		for(i=0; pr[i]*pr[i]<=n && i<m ;i++)
		{
			LL temp = n,v = 0;
			while(temp>=pr[i])
				temp /= pr[i],v++;
			ans += (v-1);
		}
		printf("Case #%d: %lld\n",++cs,ans - (n==1));
	}
	return 0;
}