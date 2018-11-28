#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;
typedef unsigned long u32;
template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}
char a[200][200];
double wp[200], owp[200], oowp[200];
int nw[200], nl[200];
int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		printf("Case #%d:\n", itest);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", a[i]);
			nl[i] = 0, nw[i] = 0;
			for (int j = 0; j < n; j++) {
				switch (a[i][j]) {
					case '0':
						nl[i]++;
						break;
					case '1':
						nw[i]++;
						break;
				}
			}
			wp[i] = nw[i] / double(nl[i] + nw[i]);
		}
		for (int i = 0; i < n; i++) {
			int k = 0;
			double sum = 0;
			for (int j = 0; j < n; j++) {
				switch (a[i][j]) {
					case '0':
						k++;
						sum += (nw[j] - 1) / double(nl[j] + nw[j] - 1);
						break;
					case '1':
						k++;
						sum += (nw[j]) / double(nl[j] + nw[j] - 1);
						break;
				}
			}
			owp[i] = sum / k;
		}
		for (int i = 0; i < n; i++) {
			int k = 0;
			double sum = 0;
			for (int j = 0; j < n; j++) {
				switch (a[i][j]) {
				case '0':
				case '1':
					k++;
					sum += owp[j];
					break;
				}
			}
			oowp[i] = sum / k;
		}
		for (int i = 0; i < n; i++) {
			printf("%.15lf\n", (wp[i] + oowp[i]) * 0.25 + 0.5 * owp[i]);
		}
	}
	return 0;
}
