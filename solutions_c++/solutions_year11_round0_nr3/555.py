#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
const int MAXN = 1007;
int g[30][30], g2[30][30];
char ord[120];
int has[30];


int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int t, n, var = 0, x;
	scanf("%d", &t);
	while (t -- ) {
		scanf("%d", &n);
		int m = 1<<30;
		int ans = 0;
		int sum = 0;
		for (int i = 0 ; i < n ; i ++ ) {
			scanf("%d", &x);
			m = min(x, m);
			ans ^= x;
			sum += x;
		}
		printf("Case #%d: ", ++var);
		if (ans) puts("NO");
		else printf("%d\n", sum-m);
	}
	return 0;
}