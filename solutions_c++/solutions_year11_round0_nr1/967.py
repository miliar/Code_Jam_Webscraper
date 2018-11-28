#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int t, n;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("outputlarge.txt", "w", stdout);

	int i, j, k, g, h;
	char ch[5];
	int d[2];
	int len[2];
	int ans;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		ans = 0;
		d[0] = d[1] = 1;
		len[0] = len[1] = 0;
		for (j = 0; j < n; ++j)
		{
			scanf("%s%d", &ch, &k);
			if (ch[0] == 'O')
				g = 0;
			else
				g = 1;
			len[g] += abs(d[g] - k) + 1;
			d[g] = k;
			if (j > 0 && g != h)
			{
				ans += len[h];
				len[g] = max(1, len[g] - len[h]);
				len[h] = 0;
			}
			h = g;
		}
		ans += len[g];
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}