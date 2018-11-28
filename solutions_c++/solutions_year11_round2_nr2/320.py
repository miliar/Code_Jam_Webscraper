#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

#pragma comment(linker, "/STACK:160000000")

const int N = 222;

int p[N];
int v[N];

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		int n, d;
		scanf("%d%d", &n, &d);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &p[i], &v[i]);
		}

		double l = 0;
		double r = 1e13;
		for (int i = 0; i < 100; ++i) {
			double q = (l + r) / 2;
			bool ok = 1;
			double cur = p[0] - q;
			for (int j = 0; j < n; ++j) {
				cur = max(cur, p[j] - q);
				cur += (v[j] - 1) * d;
				if (cur > p[j] + q) {
					ok = 0;
					break;
				}
				cur += d;
			}
			if (ok)
				r = q;
			else
				l = q;
		}

		printf("Case #%d: ", tt + 1);
		printf("%.9lf\n", l);			
	}

	return 0;
}
