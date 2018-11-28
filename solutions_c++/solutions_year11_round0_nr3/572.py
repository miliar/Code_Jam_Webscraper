#include <cstdio>

int Test, n, c, xorc, minc, totc;
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	
	scanf("%d", &Test);
	for (int kase = 1; kase <= Test; kase++) {
		xorc = totc = 0; minc = 10000000;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &c);
			if (c < minc) minc = c;
			totc += c;
			xorc ^= c;
		}
		printf("Case #%d: ", kase);
		if (xorc) puts("NO"); else printf("%d\n", totc - minc);
	}
	
	return 0;
}
