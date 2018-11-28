#include <cstdio>
using namespace std;

#define INPUT "C-large.in"
#define OUTPUT "C-large.out"
#define INF 1000001

int min(int a, int b)
{
	return a < b ? a : b;
}

void solve()
{
	int sum = 0, xorsum = 0, m = INF, n, v;

	scanf("%d", &n);
	while(n--)
	{
		scanf("%d", &v);
		sum += v;
		xorsum ^= v;
		m = min(m, v);
	}

	if(xorsum == 0)
		printf("%d\n", sum - m);
	else
		printf("NO\n");
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);

	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
