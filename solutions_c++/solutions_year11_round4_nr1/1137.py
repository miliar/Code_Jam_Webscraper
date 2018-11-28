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

const int N = 1111;

int l[N];
int r[N];
int w[N];
int ind[N];

bool cmp(int i, int j) {
	return w[i] < w[j];
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		int X, n;
		double S, R, t;
		scanf("%d%lf%lf%lf%d", &X, &S, &R, &t, &n);
		int len = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &l[i], &r[i], &w[i]);
			len += r[i] - l[i];
			ind[i] = i;		
		}
		l[n] = 0;
		r[n] = X - len;
//		printf("%d %d\n", r[n], l[n]);
		w[n] = 0;
		ind[n] = n;
		++n;
		sort(ind, ind + n, cmp);

		double ans = 0;
		for (int i = 0; i < n; ++i) {
			int d = r[ind[i]] - l[ind[i]];
			double t1 = double(d) / (R + w[ind[i]]);
//			printf("%d %lf %lf\n", d, t, t1);
			if (t1 <= t) {
				ans += t1;
				t -= t1;
			} else {
				ans += t;
				double d1 = double(t) * (R + w[ind[i]]);
				ans += double(d - d1) / (S + w[ind[i]]);
				t = 0;			
			}
		}

		printf("Case #%d: %.9lf\n", tt + 1, ans);
			
	}

	return 0;
}
