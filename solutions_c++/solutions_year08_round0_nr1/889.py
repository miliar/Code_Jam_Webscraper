#include <stdio.h>
#include <string>

using namespace std;

#define maxn 110
#define maxl 110
#define min(a,b) (a < b ? a : b)
#define inf 10000

int n, m, sol;
string a[maxn];
int c[maxn], d[maxn];
char v[maxl];

int main()
{
	freopen("univ.in", "r", stdin);
	freopen("univ.out", "w", stdout);

	int T, test;
	int i, j, k;

	scanf("%d ", &T);

	for (test = 1; test <= T; test++)
	{
		scanf("%d ", &n);

		for (i=1; i<=n; i++)
		{
			fgets(v, maxl, stdin);
			a[i] = string(v);
		}

		memset(c, 0, sizeof(c));

		scanf("%d ", &m);

		for (i=1; i<=m; i++) 
		{
			fgets(v, maxn, stdin);

			memcpy(d, c, sizeof(c));
			for (j=1; j<=n; j++) c[j] = inf;

			for (j=1; j<=n; j++) 
				if (a[j] == string(v)) 
				{
					for (k=1; k<=n; k++)
						if (j != k) c[k] = min(c[k], d[j]+1);
				}
				else c[j] = min(c[j], d[j]);
		}

		sol = inf;

		for (i=1; i<=n; i++) sol = min(sol, c[i]);

		printf("Case #%d: %d\n", test, sol);
	}

	return 0;
}
