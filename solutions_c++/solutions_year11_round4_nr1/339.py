#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

const int MAXN = 1005;

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int x, s, r, lim, n, a[MAXN], b[MAXN], w[MAXN];
		scanf("%d %d %d %d %d", &x, &s, &r, &lim, &n);
		for (int i = 0; i < n; i++)
			scanf("%d %d %d", &a[i], &b[i], &w[i]);
		int sum = 0;
		pair< int, int > q[MAXN];
		for (int i = 0; i < n; i++) {
			q[i] = make(s + w[i], b[i] - a[i]);
			sum += b[i] - a[i];
		}
		q[n] = make(s, x - sum);
		sort(q, q + n + 1);
		double l = lim, ans = 0;
		for (int i = 0; i <= n; i++) {
			int u = q[i].first, v = q[i].second;
			u = u - s + r;
			double tm = (double)v / (double)u;
			if (l - tm > 1e-9) {
				l -= tm;
				ans += tm;
			}
			else {
				double v1 = v - l * u;
				ans += v1 / (u - r + s) + (double)(v - v1) / u;
				for (int j = i + 1; j <= n; j++)
					ans += (double)q[j].second / (double)q[j].first;
				break;
			}
		}
		printf("Case #%d: %.9lf\n", t, ans);
	}
	return 0;
}

