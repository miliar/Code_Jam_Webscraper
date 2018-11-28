//google code jam 2010 qualification round 2010 c

#include <stdio.h>
const int maxn=1005;

long r,k,n,g[maxn];
long long ans;

int main()
{
	int cas,t;
	long i,j,p,q;
	bool flag;

	scanf("%d", &t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%ld%ld%ld", &r, &k, &n);
		for (i=0; i<n; i++)
			scanf("%ld", &g[i]);

		ans=0;
		p=0;
		flag=true;
		for (i=1; i<=r; i++)
		{
			j=0;
			q=p;
			while (j<=k && j+g[p]<=k)
			{
				j+=g[p];
				p=(p+1)%n;
				if (p==q) break;
			}
			ans+=j;
			if (flag && p==0)
			{
				q=r/i;
				ans*=q;
				i*=q;
				flag=false;
			}
		}
		printf("Case #%d: %lld\n", cas, ans);
	}

	return 0;
}