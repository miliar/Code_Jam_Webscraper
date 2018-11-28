#include <algorithm>
#include <cstdio>

using namespace std;

const int MAXN = 1000;

void solve()
{
	int N, v[MAXN];

	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
		scanf("%d", &v[i]);

	int xor_sum = 0, sum = 0;
	for (int i = 0; i < N; ++i)
	{
		xor_sum ^= v[i];
		sum += v[i];
	}

	if (xor_sum != 0) { printf("NO\n"); return; }

	printf("%d\n", sum - *min_element(&v[0], &v[N]));
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

    return 0;
}
