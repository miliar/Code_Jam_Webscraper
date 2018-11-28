#include <cstdio>
#include <map>

using namespace std;

const int N = 2000000;

int a[N + 1];

void init() {
	int k = 1;
	for (int i = 1; i <= N; ++i) {
		a[i] = i;
		while (10 * k <= i) k *= 10;
		int ans = a[i];
		int cur = a[i];
		for (int j = 0; j < 7; ++j) {
			cur = (cur % k) * 10 + (cur / k);
			if (cur >= k && cur < ans) ans = cur;
		}
		a[i] = ans;
	}
}

long long solve(int A, int B) {
	static int count[N + 1];
	for (int i = 1; i <= N; ++i) {
		count[i] = 0;
	}
	long long ret = 0;
	for (int i = A; i <= B; ++i) {
		++count[a[i]];
	}
	for (int i = 1; i <= N; ++i) {
		ret += 1ll * count[i] * (count[i] - 1);
	}

	return ret / 2;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	int a, b, T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %lld\n", t, solve(a, b));
	}
	return 0;
} 