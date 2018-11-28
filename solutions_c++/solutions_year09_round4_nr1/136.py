#include <cstdio>
#include <algorithm>
using namespace std;

int a[50];
int N;

void init() {
	static char buf[50];
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", buf);
		a[i] = 0;
		for (int j = 0; j < N; j++)
			if (buf[j] == '1')
				a[i] = j;
	}
}

void solve() {
	int ans = 0;
	for (int i = 0; i < N; i++) {
		int j; for (j = i; j < N && a[j] > i; j++);
		for (int k = j - 1; k >= i; k--) {
			swap(a[k], a[k + 1]);
			ans++;
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);

	int Case; scanf("%d", &Case);
	for (int i = 0; i < Case; i++) {
		init();
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}

