#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
typedef long long LL;

char mat[110][110];

double wp[110];
double owp[110];
double oowp[110];
double ans[110];
int N;
void getWp() {
	for (int i = 0; i < N; ++i) {
		int total = 0;
		int win = 0;
		for (int j = 0; j < N; ++j) {
			if (mat[i][j] != '.') {
				++total;
				if (mat[i][j] == '1') {
					++win;
				}
			}
		}
		wp[i] = 1.0 * win / total;
	}
}

void getOwp() {
	for (int i = 0; i < N; ++i) {
		double sum = 0;
		int tt = 0;
		for (int j = 0; j < N; ++j) {
			if (mat[i][j] != '.') {
				++tt;
				int total = 0;
				int win = 0;
				for (int k = 0; k < N; ++k) {
					if (k == i) {
						continue;
					}
					if (mat[j][k] != '.') {
						++total;
						if (mat[j][k] == '1') {
							++win;
						}
					}
				}
				sum += win * 1.0 / total;
			}
		}
		owp[i] = sum / tt;
	}
}

void getOowp() {
	for (int i = 0; i < N; ++i) {
		int total = 0;
		double sum = 0;
		for (int j = 0; j < N; ++j) {
			if (mat[i][j] != '.') {
				++total;
				sum += owp[j];
			}
		}
		oowp[i] = sum / total;
	}
}

int main() {
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int bb = 1;
	while (T--) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%s", mat[i]);
		}
		getWp();
		getOwp();
		getOowp();
        printf("Case #%d:", bb++);
		puts("");
		for (int i = 0; i < N; ++i) {
			printf("%.7lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
    }
    return 0;
}