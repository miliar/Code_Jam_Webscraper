/*
 * A.cpp
 *
 *  Created on: 2011-5-21
 *      Author: stm
 */

#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

const int MAXN = 110;
const double EPS = 1e-6;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int n, T;
	string a[MAXN];
	double WP[MAXN], OWP[MAXN], OOWP[MAXN], RPI[MAXN];
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		for (int i = 0; i < n; ++i) {
			double tot = double(0.0), win = double(0.0);
			for (int j = 0; j < n; ++j)
				if (a[i][j] == '1') {
					tot += double(1.0);
					win += double(1.0);
				}
				else
				if (a[i][j] == '0'){
					tot += double(1.0);
				}
			//cout << i << ' '  << win << ' ' << tot << endl;

			WP[i] = win / tot;
		}

		for (int i = 0; i < n; ++i) {
			double now = double(0.0), cnt = double(0.0);
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.') {
					cnt += double(1.0);
				double tot = double(0.0), win = double(0.0);
				for (int k = 0; k < n; ++k)
					if (k != i)
						if (a[j][k] == '1') {
							tot += double(1.0);
							win += double(1.0);
						}
						else if (a[j][k] == '0'){
							tot += double(1.0);
						}
			//	printf("%.6lf .. %.6lf\n", win, tot);
				now += win / tot;
			}
		//	cout << now << ' ' << cnt << endl;
			OWP[i] = now / cnt;
		//	printf("%.6lf\n", OWP[i]);
		}

		for (int i = 0; i < n; ++i)
		{
			double now = double(0.0), cnt = double(0.0);
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.') {
					now += OWP[j];
					cnt += double(1.0);
				}
			//cout << now << ' ' << cnt << endl;
			OOWP[i] = now / cnt;
		}

		for (int i = 0; i < n; ++i)
			RPI[i] = double(0.25) * WP[i] + double(0.5) * OWP[i] + double(0.25) * OOWP[i];

		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i)
			printf("%.7lf\n", RPI[i]);
	}
	return 0;
}
