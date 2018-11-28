//============================================================================
// Name        : gcj@2011-1B-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#define M 105
using namespace std;
typedef long long LL;

double wp[M];
double owp[M];
double oowp[M];

int n;
char map[M][M];

double getOWP(int j, int index) {
	int tot = 0;
	int cnt = 0;
	for (int i = 0; i < n; i ++) {
		if (i == index) {
			continue;
		}
		if (map[j][i] != '.') {
			tot ++;
		}
		if (map[j][i] == '1') {
			cnt ++;
		}
	}
	return 1.0 * cnt / tot;
}

int main() {
//	freopen("test.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	int index = 1;
	scanf ("%d", &T);
	while (T --) {
		scanf ("%d", &n);
		for (int i = 0; i < n; i ++) {
			scanf ("%s", map[i]);
		}

		for (int i = 0; i < n; i ++) {
			int tot = 0;
			int cnt = 0;
			double owpT = 0.0;
			for (int j = 0; j < n; j ++) {
				if (map[i][j] != '.') {
					tot ++;
					owpT += getOWP(j ,i);
				}
				if (map[i][j] == '1') {
					cnt ++;
				}
			}
			wp[i] = 1.0 * cnt / tot;
			owp[i] = 1.0 * owpT / tot;
		}

		for (int i = 0; i < n; i ++) {
			int cnt = 0;
			double tmp = 0.0;
			for (int j = 0; j < n; j ++) {
				if (map[i][j] != '.') {
					tmp += owp[j];
					cnt ++;
				}
			}
			oowp[i] = 1.0 * tmp / cnt;
		}
		printf ("Case #%d:\n", index ++);
		for (int i = 0; i < n; i ++) {
//			cerr << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
			double tmp = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf ("%.6f\n", tmp);
		}
	}
	return 0;
}
