#include <cstdio>
int Test, kase, n, a;
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	
	scanf("%d", &Test);
	for (int kase = 1; kase <= Test; kase++) {
		scanf("%d", &n);
		int cnt = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a);
			if (a != i) cnt++;
		}
		printf("Case #%d: %d.000000\n", kase, cnt);
	}
	
	return 0;
}
