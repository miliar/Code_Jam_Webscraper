#include <cstdio>
#include <cstring>


int nt;

int n, k, L, t;
int x[100], v[100];

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d %d %d", &n, &k, &L, &t);

		for(int i = 0; i < n; i++) scanf("%d", &x[i]);
		for(int i = 0; i < n; i++) scanf("%d", &v[i]);

		int res = 0;

		int p = n - 1;
		
		while(p >=0 && k > 0)
		{
			int tm = (L - x[p] + v[p] - 1) / v[p];
			
			if (tm <= t)
			{
				p--;
				k--;
				continue;
			}

			res += k;
			p--;
		}

		if (k > 0) puts("IMPOSSIBLE"); else printf("%d\n", res);
	}

	return 0;	
}