#include<stdio.h>
#include<algorithm>
const int maxn = 805;
int n;
int a[maxn], b[maxn];
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &b[i]);
		}
		std::sort(a, a + n);
		std::sort(b, b + n);
		long long ans = 0;
		for (int i = 0; i < n; i++) {
			long long t = b[n - i - 1];
			ans += t * a[i];
		}
		printf("Case #%d: %lld\n", casen, ans);
	}
	return 0;
}
