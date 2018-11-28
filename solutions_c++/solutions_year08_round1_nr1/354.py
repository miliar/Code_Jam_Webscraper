#include <stdio.h>
#include <algorithm>
using namespace std;
int v1[900], v2[900];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas, tex, n, i, ans;
	for (scanf("%d", &cas), tex = 1; tex <= cas; ++tex) {
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
			scanf("%d", &v1[i]);
		for (i = 0; i < n; ++i)
			scanf("%d", &v2[i]);
		sort(&v1[0], &v1[n]); sort(&v2[0], &v2[n]);
		for (i = 0, ans = 0; i < n; ++i)
			ans += v1[i] * v2[n - i - 1];
		printf("Case #%d: %d\n", tex, ans);
	}
	return 0;
}