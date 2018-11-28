#include <stdio.h>
#include <string.h>
const int MAXN = 1050;
int ans;
int n;
int p[MAXN][MAXN];
int b[MAXN][MAXN];
int m[MAXN];
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		printf("Case #%d: ", ca);
		scanf("%d", &n);
		for (int i = 0; i < (1 << n); ++i) scanf("%d", &m[i]);
		for (int i = 0; i < (1 << n); ++i) m[i] = n - m[i];
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < (1 << (n - i - 1));  ++j)
				scanf("%d", &p[i][j]);
		memset(b, 0, sizeof(b));
		ans = 0;
		for (int i = 0; i < (1 << n); ++i)
		{
			int cnt = m[i];
			for (int j = 0; j < n; ++j)
			{
				if (cnt <= 0) break;
				if (!b[n - j - 1][i >> (n - j)])
				{
					b[n - j - 1][i >> (n - j)] = 1;
					for (int k = 0; k < (1 << n); ++k)
						if ( (i >> (n - j)) == (k >> (n - j))) --m[k];
					++ans;
					--cnt;
				}
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}
