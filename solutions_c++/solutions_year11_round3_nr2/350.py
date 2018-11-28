#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long Int64;

const int maxn = 2000000;

int a[maxn], seq[maxn];
int L, N, C, len;
Int64 t;

void init() {
	scanf("%d %I64d %d %d", &L, &t, &N, &C);
	for (int i = 0; i < C; i++)
		scanf("%d", &a[i]);
}

void work() {
	Int64 sum = 0;
	for (int i = 0; i < N; i++)
		sum += a[i % C] * 2;
	if (L == 0) {
		printf("%I64d\n", sum);
		return;
	}
	int start = 0;
	sum = 0;
	for (start = 0; start < N; start++)
		if (sum + a[start % C] * 2 > t) break;
		else sum += a[start % C] * 2;
	if (start >= N) {
		printf("%I64d\n", sum);
		return;
	}
	len = 0;
	for (int j = start + 1; j < N; j++)
		seq[len++] = a[j % C];
	sort(seq, seq + len);
	Int64 left = t - sum;
	Int64 ans1 = sum + (a[start % C] - left / 2) + left;
	for (int i = 0; i < len; i++) {
		ans1 += seq[len - 1 - i] * 2;
		if (i < L - 1) ans1 -= seq[len - 1 - i];
	}
	Int64 ans2 = sum + a[start % C] * 2;
	for (int i = 0; i < len; i++) {
		ans2 += seq[len - 1 - i] * 2;
		if (i < L) ans2 -= seq[len - 1 - i];
	}
	if (ans1 < ans2) printf("%I64d\n", ans1);
	else printf("%I64d\n", ans2);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		init();
		work();
	}
	return 0;
}