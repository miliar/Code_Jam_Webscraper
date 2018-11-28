#include <cstdio>

int ttt, T;
int v[16];
int n;

void work()
{
	int ans = -1, tot = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%d", &v[i]);
	for (int i = 0; i < n; ++i) tot ^= v[i];
	for (int subset = 0; subset < (1 << n) - 1; ++subset) {
		int xor = 0, sum = 0;
		for (int i = 0; i < n; ++i) if (subset & (1 << i)) {
			xor ^= v[i];
			sum += v[i];
		}
		if (xor == (tot ^ xor) && sum > ans)
			ans = sum;
	}
	printf("Case #%d: ", ++ttt);
	if (ans == -1)
		printf("NO\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	while (T--) work();
}