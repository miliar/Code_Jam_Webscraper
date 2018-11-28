#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 128;

int n, cas;
char tb[MAXN][MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%s", tb[i]);
		for (int i = 0; i < n; ++i) {
			double wc = 0, pc = 0;
			for (int j = 0; j < n; ++j) {
				if (tb[i][j] != '.') {
					pc ++;
					if (tb[i][j] == '1')
						wc++;
				}
			}
			wp[i] = wc / pc;
		}
		for (int i = 0; i < n; ++i) {
			double oc = 0, sum = 0;
			for (int j = 0; j < n; ++j) {
				if (tb[i][j] != '.') {
					double wc = 0, pc = 0;
					for (int k = 0; k < n; ++k) {
						if (k != i) {
							if (tb[j][k] != '.') {
								pc++;
								if (tb[j][k] == '1')
									wc++;
							}
						}
					}
					oc ++;
					sum += wc / pc;
				}
			}
			owp[i] = sum / oc;
		}
		for (int i = 0; i < n; ++i) {
			double oc = 0, sum = 0;
			for (int j = 0; j < n; ++j) {
				if (tb[i][j] != '.') {
					oc ++;
					sum += owp[j];
				}
			}
			oowp[i] = sum / oc;
		}
		printf("Case #%d:\n", c);
		for (int i = 0; i < n; ++i) {
			double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.8lf\n", rpi);
		}
	}
	return 0;
}