#include <cstdio>
#include <cstring>

const int maxn = 100;

int casei, cases, n, ans;
char st[maxn + 1];
int num[maxn + 1];

inline void init() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf(" %s", st);
		num[i] = 0;
		for (int j = strlen(st) - 1; j >= 0; --j) if (st[j] == '1') {
			num[i] = j;
			break;
		}
	}
}

inline void process() {
	ans = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = i; j < n; ++j) if (num[j] <= i) {
			ans += j - i;
			for (int k = j; k > i; --k) num[k] = num[k - 1];
			break;
		}
	}
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
