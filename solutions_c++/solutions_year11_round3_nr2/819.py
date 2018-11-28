#include <algorithm>
#include <cstdio>

using namespace std;

int L, N, C, a[1000], d[1000000], r[1000000];
long long t;

void solve()
{
	for (int i = 0; i < N; ++i) d[i] = a[i%C];

	long long cur_d = 0;
	int bi = -1;

	for (int i = 0; i <= N; ++i)
	{
		if (cur_d > t/2) { bi = i-1; break; }
		if (i < N) cur_d += d[i];
	}

	if (bi == -1) { printf("%lld\n", cur_d * 2); return; }

	int nr = 1;
	r[0] = cur_d - t/2;

	for (int i = bi+1; i < N; ++i) r[nr++] = d[i];

	sort(&r[0], &r[nr]);
	reverse(&r[0], &r[nr]);

	cur_d = 0;
	for (int i = 0; i < N; ++i) cur_d += d[i];

	cur_d *= 2;

	for (int i = 0; i < L; ++i) cur_d -= r[i];

	printf("%lld\n", cur_d);
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t1 = 1; t1 <= T; ++t1)
	{
		scanf("%d%lld%d%d", &L, &t, &N, &C);

		for (int i = 0; i < C; ++i)
			scanf("%d", &a[i]);

		printf("Case #%d: ", t1);
		solve();
	}

	return 0;
}
