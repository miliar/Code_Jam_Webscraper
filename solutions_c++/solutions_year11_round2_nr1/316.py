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

const int N = 111;

char s[N][N];
double wp[N];
double owp[N];
double oowp[N];
int o[N];
int w[N];

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		int n;
		scanf("%d\n", &n);
		for (int i = 0; i < n; ++i) {
			gets(s[i]);
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			o[i] = 0;
			w[i] = 0;
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				o[i] += (s[i][j] != '.');
				w[i] += (s[i][j] == '1');
			}
			wp[i] = double(w[i]) / o[i];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (s[i][j] != '.') {
					owp[i] += double(w[j] - (s[j][i] == '1')) / (o[j] - 1);
				}
			}
			owp[i] /= o[i];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (s[i][j] != '.') {
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= o[i];
		}

		printf("Case #%d:\n", tt + 1);

		for (int i = 0; i < n; ++i) {
//			printf("%lf %lf %lf\n", wp[i], owp[i], oowp[i]);
			printf("%.9lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	
	}

	return 0;
}
