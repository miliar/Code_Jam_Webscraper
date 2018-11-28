#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;

int a[1001], b[1001], n;

int solve() {
	int ret = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			if (a[i] > a[j] && b[i] < b[j])
				++ret;
		}
	return ret;
}

int main() {
	int test, t;
	freopen("al.in", "r", stdin);
	freopen("al.out", "w", stdout);
	for (scanf("%d", &test), t = 1; t <= test; t++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d", &a[i], &b[i]);
		printf("Case #%d: %d\n", t, solve());
	}

	return 0;
}
