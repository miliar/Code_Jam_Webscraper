#include <stdio.h>

int nxt(int x, int b) {
	return x / 10 + ((x % 10) * b);
}

int len(int x) {
	int t = 1;
	x /= 10;
	while (x) {
		x/=10;
		t*=10;
	}
	return t;
}

int main() {
	int t,ca = 0, a, b, num, i, j, x;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &a, &b);
		num = 0;
		for (i=a;i<=b;++i) {
			x = len(i);
			for (j = nxt(i,x); j != i; j = nxt(j,x)) {
				if (j >= a && j <= b && j > i) ++num;
			}
		}
		printf("Case #%d: %d\n", ++ca, num);
	}
	return 0;
}
