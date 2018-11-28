#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 6;
const int maxlen = 1100;
const int oo = 2147483647;

int casei, cases, n, m, ans;
int per[maxn];
char st[maxlen], newst[maxlen];

inline void init() {
	scanf("%d %s", &n, st);
	m = strlen(st);
}

inline void calc() {
	for (int i = 0; i < m / n; ++i) {
		int k = i * n;
		for (int j = 0; j < n; ++j) newst[k + j] = st[k + per[j]];
	}
	int cnt = 0;
	for (int i = 1; i < m; ++i) if (newst[i] != newst[i - 1]) ++cnt;
	if (cnt < ans) ans = cnt;
}

inline void process() {
	ans = oo;
	for (int i = 0; i < n; ++i) per[i] = i;

	while (true) {
		calc();
		int i, j, k, t;
		i = n - 1;
		while (i > 0)
			if (per[i] < per[i - 1]) --i;
			else break;
		if (i == 0) break;

		k = i - 1;
		for (j = i; j < n; ++j) if (per[j] > per[i - 1])
			if (k == i - 1 || per[j] < per[k]) k = j;
		t = per[i - 1]; per[i - 1] = per[k]; per[k] = t;
		sort(per + i, per + n);
	}
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans + 1);
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("D-small-attempt0.in", "r", stdin); freopen("D-small.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
