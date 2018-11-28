#include <stdio.h>
int st[11111], stn;

int get() {
	int i, t = 1;
	for (i = stn; i >= 1; i--) {
		if (st[i] == 1) {
			t = 1 - t;
		} else {
			t = 1;
		}		
	}
	return t;
}

void gcd(int a, int b) {
	if (a < b) {
		int t = a;
		a = b, b = t;
	}
	if (!b) {
		return;
	}
	st[++stn] = a / b;
	gcd(b, a % b);
}

int main() {
	int tn, a1, a2, b1, b2;
	int a, b, ans, prob = 0;
//	freopen("c.in", "r", stdin);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	for (scanf("%d", &tn); tn--; ) {
		ans = 0;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		printf("Case #%d: ", ++prob);
		for (a = a1; a <= a2; a++) {
			for (b = b1; b <= b2; b++) {
				stn = 0;
				gcd(a, b);
				ans += get();
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
