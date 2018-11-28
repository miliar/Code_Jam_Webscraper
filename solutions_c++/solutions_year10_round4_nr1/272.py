// GCJ 2010 2R
// A. Elegant Diamond
// wookayin

#include <algorithm>
#include <stdio.h>
#include <memory.h>
using namespace std;

int n;
int sz[111];
int a[111][111];
int l[111], r[111];

int goodrange(int x, int y)
{
	if(x < 1 || x >= 2*n)
		return false;
	return l[x] <= y && y <= r[x];
}

int get(int cx, int cy)
{
	int maxdist = 0;

	for(int i=1; i<=2*n-1; ++i)
	{
		for(int j=l[i]; j<=r[i]; j+=2)
		{
			int ii = 2 * cx - i;
			int jj = 2 * cy - j;

			maxdist = max(maxdist, abs(ii-cx) + abs(jj-cy));
			
			if(goodrange(ii, jj) && a[ii][jj] != -1 && a[i][j] != a[ii][jj])
				return 987654321;
			if(goodrange(i, jj) && a[i][jj] != -1 && a[i][j] != a[i][jj])
				return 987654321;
			if(goodrange(ii, j) && a[ii][j] != -1 && a[i][j] != a[ii][j])
				return 987654321;
			
		}
	}
	return (maxdist+1) * (maxdist + 1) - n*n;
//	int total = (maxdist + 1) * (maxdist + 1) - seen;
//	return total + hit;
}

int go()
{
	int ans = 987654321;
	for(int i=0; i<=2*n; ++i)
	{
		for(int j=0; j<=2*n; ++j)
		{
			int t = get(i, j);
			ans = min(ans, t);
		}
	}
	return ans;
}

int main()
{
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt)
	{
		fprintf(stderr, "%d\n", tt);
		scanf("%d", &n);
		memset(a, -1, sizeof(a));
		memset(l, 0, sizeof(l));
		memset(r, 0, sizeof(r));
		for(int i=1; i<=2*n-1; ++i)
		{
			sz[i] = min(i, 2*n-i);
			l[i] = n - sz[i] + 1;
			r[i] = l[i] + 2 * (sz[i] - 1);

			for(int x = n - sz[i] + 1, q=0; q<sz[i]; ++q, x+=2)
			{
				scanf("%d", &a[i][x]);
			}
		}
		printf("Case #%d: %d\n", tt, go());
	}
	return 0;
}
