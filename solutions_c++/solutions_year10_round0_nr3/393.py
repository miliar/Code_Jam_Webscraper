#include <cstdio>
#include <cstring>

using namespace std;

int R, k, N;
long long g[1000], ans, per_sum[1000];
int per_step[1000];

void solve()
{
	ans = 0;

	int step = 0, cur = 0;
	memset(per_step, -1, sizeof(per_step));
	do
	{
		per_step[cur] = step; per_sum[cur] = ans;

		int i = cur;
		long long sum = 0;
		do
		{
			sum += g[i];
			i = (i+1) % N;
		} while (i != cur && sum+g[i] <= k);

		--R; cur = i; ans += sum; ++step;

		if (per_step[i] != -1)
		{
			int per_len = step - per_step[i], per_size = R / per_len;
			long long per_add = ans - per_sum[i];

			R -= per_size * per_len;
			ans += per_size * per_add;
		}
	} while (R != 0);

	printf("%lld\n", ans);
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
		scanf("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; ++i) scanf("%lld", &g[i]);
		solve();
	}

	return 0;
}
