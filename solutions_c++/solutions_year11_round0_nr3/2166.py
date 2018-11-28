#include <cstdio>
#include <algorithm>

using namespace std;

void solve()
{
	int n, v, r = 0, s = 0, m = 999999999;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &v);
		r ^= v;
		s += v;
		m = min(m, v);
	}
	printf(r == 0 ? "%d" : "NO", s - m);
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}