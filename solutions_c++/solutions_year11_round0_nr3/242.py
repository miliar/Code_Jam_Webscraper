#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
int s[1010];
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int n, i, j;
		scanf("%d", &n);
		int sum = 0, sum2 = 0;
		for (i = 0; i < n; ++i) {
			scanf("%d", &s[i]);
			sum = sum ^ s[i];
			sum2 += s[i];
		}
		int ans = 0;
		for (i = 0; i < n; ++i) {
			if ((sum ^ s[i]) == s[i])
				ans = max(ans, sum2 - s[i]);
		}
		if (ans > 0)
			printf("Case #%d: %d\n", t + 1, ans);
		else
			printf("Case #%d: NO\n", t + 1);
	}
}
