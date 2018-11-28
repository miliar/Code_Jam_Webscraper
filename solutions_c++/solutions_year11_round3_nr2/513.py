/*
 * B.cpp
 *
 *  Created on: 2011-5-22
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXN = 100100;
double EPS = 1e-7;
int T, c, n, L;
double d[MAXN], s[MAXN];
double t;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &T);
	double aa;
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d%lf%d%d", &L, &t, &n, &c);
		for (int i = 0; i < c; ++i) {
			scanf("%lf", &aa);
			for (int k = 0; k * c + i < n; ++k)
				d[k * c + i] = aa;
		}

		double ans = double(0.0);
		s[0] = double(0.0);
		for (int i = 0; i < n; ++i) {
			ans += double(2.0) * d[i];
	//		printf("%.0lf ", d[i]);
			s[i + 1] = s[i] + double(2.0) * d[i];
		}
		//puts("");
//		printf("%.0lf\n" ,ans);

		printf("Case #%d: ", tt);

		if (L == 0 || s[n] <= t + EPS)
			printf("%.0lf\n", ans);
		else
		if (L == 1) {
			double now = 0.0;
			for (int i = 0; i < n; ++i) {
				if (s[i + 1] <= t + EPS) continue;
				double time = s[i];
				if (t > time + EPS) time = t;
				double dd = (time - s[i]) / double(2.0);
				if (d[i] - dd > now + EPS) now = d[i] - dd;
			}
			ans -= now;
			printf("%.0lf\n", ans);
		}
		else
		if (L == 2) {
			double now = ans;
			for (int i = 0; i < n; ++i) {
				double time = s[i];
				if (t > time + EPS) time = t;
				double dd1 = (time - s[i]) / double(2.0);
				now -= (d[i] - dd1);
				for (int j = i; j < n; ++j)
					s[j] -= (d[i] - dd1);

				if (i < n - 1) {
					for (int j = i + 1; j < n; ++j) {
						double time = s[j];
						if (t > time + EPS) time = t;
						double dd2 = (time - s[j]) / double(2.0);
						now -= (d[j] - dd2);
						if (now < ans - EPS) ans = now;
						now += (d[j] - dd2);
					}
				}
				else
					if (now < ans - EPS) ans = now;

				for (int j = i; j < n; ++j)
					s[j] += (d[i] - dd1);

				now += (d[i] - dd1);
			}
			printf("%.0lf\n", ans);
		}
	}
	return 0;
}
