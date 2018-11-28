#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define MAXN 64

int solve(void)
{
	int n, t, k, b;
	scanf("%d%d%d%d", &n, &k, &b, &t);
	int d[MAXN], v[MAXN];
	for (int i = 0; i < n; i++) scanf("%d", &d[i]);
	for (int i = 0; i < n; i++) scanf("%d", &v[i]);
	int imp[MAXN];
	int numImp = 0;
	for (int i = 0; i < n; i++) {
		imp[i] = ((b - d[i]) > (t * v[i]));
		numImp += imp[i];
	}
	if (k == 0) return 0;
	if (k > n - numImp) return -1;
	int start = n;
	int ans = 0;
	while (k--) {
		start--;
		while (imp[start]) start--;
		for (int i = start + 1; i < n; i++) ans += imp[i];
	}
	return ans;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int s = solve();
		if (s == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", s);
	}
	return 0;
}
