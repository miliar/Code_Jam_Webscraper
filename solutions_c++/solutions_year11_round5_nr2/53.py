#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000];
int N;

int pos[1000]; int head, tail;

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &a[i]);

	if (N == 0) {
		printf("0\n");
		return;
	}

	sort(a, a + N);

	int lastcount = 0; head = tail = 0;
	int ans = 1000000;

	for (int i = 0; i < N; ) {
		int count = 1, j = i;
		while (j + 1 < N && a[j + 1] == a[j]) j++, count++;

		if (i && a[i - 1] != a[i] - 1) {
			for (; head < tail; head++) ans = min(ans, a[i - 1] - pos[head] + 1);
			lastcount = 0;
		}

		for (int k = count; k < lastcount; k++) {
			ans = min(ans, a[i - 1] - pos[head] + 1);
			head++;
		}

		for (int k = lastcount; k < count; k++) {
			pos[tail++] = a[i];
		}

		lastcount = count;
		i = j + 1;
	}

	for (; head < tail; head++) ans = min(ans, a[N - 1] - pos[head] + 1);

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
