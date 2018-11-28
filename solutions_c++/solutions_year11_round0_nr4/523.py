#include <stdio.h>
#include <string.h>

const int MAXN = 1001;

int n;
int a[MAXN];
bool used[MAXN];

double fact(int n) {
	double ret = 1;
	for (int i = 1; i <= n; ++i)
		ret *= i;
	return ret;
}

int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		printf("Case #%d: ", k + 1);
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d", &a[i]);
		memset(used, false, sizeof(used));
		double ans = 0;
		for (int i = 1; i <= n; ++i) {
			if (a[i] != i) ans = ans + 1;
		}
		printf("%lf\n", ans);
	}
	return 0;
}
