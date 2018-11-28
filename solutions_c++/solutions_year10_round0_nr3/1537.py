#include <stdio.h>

int t, n, k, r, g[1000], p, rx;
long long  x[1000], y[1000], res;

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		scanf(" %d %d %d", &r, &k, &n);
		for(int i=0; i<n; i++) { scanf(" %d", &g[i]); x[i]=y[i]=0; }
		p=rx=res=0;
		while((rx<r) && (!y[p]))
		{
			int f=k, pp=p;
			x[pp]=res; y[pp]=++rx;
			while(f>=g[p])
			{
				res+=g[p]; f-=g[p]; p=(p+1)%n;
				if (p==pp) break;
			}
		}

		{
			int l=rx-y[p]+1;
			int l1=(r-rx)/l;
			// printf("-> %3dl*%3dl1 %3lldres %3drx %3dp %3lld  ", l, l1, res, rx, p, (res-x[p])*l1);
			res+=(res-x[p])*l1;
			rx+=l1*l;
		}

		while((rx<r))
		{
			int f=k, pp=p;
			while(f>=g[p])
			{
				res+=g[p]; f-=g[p]; p=(p+1)%n;
				if (p==pp) break;
			}
			rx++;
		}
		printf("Case #%d: %lld\n", cs, res);
	}
	return 0;
}
