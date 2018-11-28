#include <cstdio>

int min(int x, int y) { return x < y ? x : y; }
int max(int x, int y) { return x < y ? y : x; }

int n, s, p, P;

int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		scanf("%d%d%d", &n, &s, &p);
		P = 3*p - 2;
		int cnt1 = 0, cnt2 = 0;
		for (int i = 0; i < n; ++i) {
			int x; scanf("%d", &x);
			if (x >= P) ++cnt1;
			else if (x >= max(3*p - 4, p)) ++cnt2;
		}
		printf("Case #%d: %d\n", ++cas, cnt1 + min(s, cnt2));
	}
	return 0;
}
