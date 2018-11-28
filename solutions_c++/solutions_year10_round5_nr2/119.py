#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

#define mp make_pair
#define pb push_back

typedef long long i64;

const int M = 2000001;
int a[100];
int u[M];
int d[M];
int q[M];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		i64 l;
		int n;
		scanf("%lld %d", &l, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		
		int h = 0, t = 0;
		u[0] = tt + 1;
		d[0] = 0;
		q[t++] = 0;
		while (h < t) {
			int v = q[h++];
			for (int i = 0; i < n; ++i) {
				if (v + a[i] >= M) break;
				if (u[v + a[i]] != tt + 1) {
					u[v + a[i]] = tt + 1;
					d[v + a[i]] = d[v] + 1;
					q[t++] = v + a[i];
				}
			}
		}
		i64 result = -1;
		for (int i = 0; i < n; ++i) {
			i64 x = max((l - M), 0) / a[i];
			i64 r = x;
			x = l - x * a[i];
			while (x >= M) {
				x -= a[i];
				++r;
			}
			if (u[x] == tt + 1) {
				r += d[x];
				if ((result == -1) || (result > r)) {
					result = r;
				}
			}
		}
		
		printf("Case #%d: ", tt + 1);
		if (result == -1) printf("IMPOSSIBLE\n");
		else printf("%lld\n", result);
		fflush(stdout);
	}
	return 0;
}
