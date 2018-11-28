# include <stdio.h>
# include <string.h>
# include <stdlib.h>

int n,m,s,k,tk,ts,ans,t,pmax,pmin,kase=0;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	scanf("%d", &n);

	while (n)
	{
		scanf("%d%d%d", &m, &s, &k);

		if (k==1) pmin=1; else pmin=2*(k-2)+k; pmax=2*(k+2)+k;

		ts=ans=0;

		for (int i=0; i<m; i++)
		{
			scanf("%d", &t);

			if (t>pmax) ans++; else
			if (t<pmin) continue; else
			{
				if (t%3) tk=t/3+1; else tk=t/3;

				if (tk>=k) ans++; else
				if (tk==k-1) ts++;
			}
		}

		if (ts>=s) ans+=s; else ans+=ts;

		printf("Case #%d: %d\n", ++kase, ans);
		
		n--;
	}
}