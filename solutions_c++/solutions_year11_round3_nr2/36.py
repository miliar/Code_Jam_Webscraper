#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
__int64  L, t, N, C;
__int64 D[1010];
__int64 calc(int a, int b)
{
	__int64 ans = 0;
	for (int i = 0; i < N; ++i)
	{
		if (ans > t && (a == i || b == i)) ans += D[i];
		else
		{
			if (ans + D[i] * 2 < t || (a != i && b != i)) ans += D[i] * 2;
			else
			{
				ans = t + D[i] - (t - ans) / 2;
			}
		}
	}
	return ans;
}
void solve()
{
	scanf ("%I64d%I64d%I64d%I64d", &L, &t, &N, &C);
	__int64 ans = 1e18;
	for (int i = 0; i < C; ++i)
	{
		scanf ("%I64d", &D[i]);
	}
	for (int i = C; i < N; ++i)
	{
		D[i] = D[i - C];
	}
	if (L == 0)
	{
		printf ("%I64d\n", calc(-1, -1));
		return;
	}
	if (L == 1)
	{
		for (int i = 0; i < N; ++i)
		{
			
				ans = min(ans, calc(i, -1));
		}
		printf ("%I64d\n", ans);
		return;
	}
	for (int i = 0; i < N; ++i)
	{
		for (int j = i + 1; j < N; ++j)
		{
			ans = min(ans, calc(i, j));
		}
	}
	printf ("%I64d\n", ans);
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
		fprintf(stderr, "%d\n", i);
	}
	return 0;
}