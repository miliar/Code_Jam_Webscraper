#include <stdio.h>
#include <string.h>

int a[1010], time[1010], s[1010], g[1010];

int main()
{
	freopen("c.in", "r", stdin);freopen("c.out", "w", stdout);
	int T, i, q, tot, now, cas, n, r, k, t;
	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (i=0; i<n; i++) scanf("%d", &g[i]);
		memset(s, 0, sizeof(s));
		q=0;
		tot=0;
		for (t=0; t<r; t++)
		{
			if (s[q]>0) break;
			a[t]=q;
			time[q]=t;			
			s[q]=tot;

			now=0;
			for (i=0; i<n; i++)
			{
				now+=g[(q+i)%n];
				if (now>k) break;
			}
			if (now>k) now -= g[(q+i)%n];
			tot+=now;
			q=(q+i)%n;
		}
		int ans;
		if (t==r) ans=tot;
		else 
		{
			int circle=tot-s[q];
			ans=s[q]+(r-time[q])/(t-time[q])*circle+ s[a[time[q]+(r-time[q])%(t-time[q])]] - s[q];
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
