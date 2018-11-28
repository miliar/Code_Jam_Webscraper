#include <stdio.h>
#include <utility>

void solve()
{
	static int G[1000];
	static std::pair<int, int> T[1000];
	int r, k ,n;
	long long w = 0;
	scanf("%d %d %d", &r, &k, &n);
	for (int i = 0 ; i < n; i++)
		scanf("%d", &G[i]);
	for (int rot = 0, i, c; rot < n; rot++)
	{
		for (i = 0, c = 0; i < n && c + G[(rot + i) % n] <= k; i++)
			c += G[(rot + i) % n];
		T[rot].first = c;
		T[rot].second = (rot + i) % n;
	}
	for (int rot = 0; r--; rot = T[rot].second)
		w += T[rot].first;
	printf("%lld\n", w);
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}