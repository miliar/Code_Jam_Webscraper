#include <cstdio>

int best[1005];


void solve() {
	int r, n, k;
	int npeople[1005];
	long long rew[1005];
	
	scanf("%d %d %d", &r, &k, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &npeople[i]);

	for (int i = 0; i < n; i++) {
		long long sum = 0;
		int j;
		for (j = 0; j < n && sum + npeople[ (i+j) % n ] <= k; j++)
			sum += npeople[ (i+j) % n ];
		best[i] = j;
		rew[i] = sum;
	}

	long long ans = 0ll;
	int pos = 0;
	for (int i = 0; i < r; i++) {
//		printf("Ride from group [%d] with %d groups\n", pos, best[pos]);
		ans += rew[pos];
		pos += best[pos];
		pos %= n;
	}

	printf("%lld\n", ans);
}



int main() {
	freopen("q3.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}

	return 0;
}

