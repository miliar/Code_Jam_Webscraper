#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
int test;
int n, s, p;
int a[200];
int c1, c2;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		scanf("%d %d %d", &n, &s, &p);
		c1 = c2 = 0;
		for (int i = 1; i <= n ; ++i) {
			scanf("%d", &a[i]);
			if (a[i] >= 3 * p - 2) ++c1;
			else if (a[i] >= 3 * p - 4 && a[i] > 1	) ++c2;
		}
		printf("Case #%d: %d\n", t, c1 + min(c2, s));
	}
	return 0;
}