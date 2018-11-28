#include <cassert>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
typedef pair<int, int> ii;
typedef long long LL;

int a[42];
char ee[42];

int main() {
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		int n;
		scanf("%d\n", &n);
		for (int i = 1; i <= n; i++) {
			gets(ee);
			a[i] = 0;
			for (int j = 0; j < n; j++) if (ee[j] == '1') a[i] = (j + 1);
		}
		int ans = 0;
		for (int k = 1; k <= n; k++) {
			int mi = -1;
			for (int i = k; i <= n; i++) if (a[i] <= k) {
				mi = i;
				break;
			}
			ans += mi - k;
			for (int i = mi; i > k; i--) a[i] = a[i - 1];
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
