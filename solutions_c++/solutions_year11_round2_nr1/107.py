#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)>(b)?(a):(b))

const int MAXN = 111;

int n;
char s[MAXN][MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
			wp[i] = owp[i] = oowp[i] = 0;
		}
		for (int i = 0; i < n; ++i) {
			int p = 0, k = 0;
			for (int j = 0; j < n; ++j)
				if (s[i][j] != '.') {
					++p;
					k += s[i][j] == '1';
			}
			if (p != 0) wp[i] = (double) k / p;
			else wp[i] = 0;
		}
		for (int i = 0; i < n; ++i) {
			int cnt = 0;
			for (int j = 0; j < n; ++j) 
				if (s[i][j] != '.') {
					++cnt;
					int p = 0, q = 0;
					for (int k = 0; k < n; ++k) {
						if (k != i && s[j][k] != '.') {
							++p; 
							q += s[j][k] == '1';
						}
					}
					if (p != 0) owp[i] += (double) q / p;
			}
			if (cnt != 0) owp[i] /= cnt;
		}
		for (int i = 0; i < n; ++i) {
			int cnt = 0;
			for (int j = 0; j < n; ++j)
				if (s[i][j] != '.') {
					oowp[i] += owp[j];
					++cnt;
				}
			if (cnt > 0) oowp[i] /= cnt;
		}
		printf("Case #%d:\n", tt);
		for (int i = 0; i < n; ++i) {
//			printf("%.5lf %.5lf %.5lf\n", wp[i], owp[i], oowp[i]);
			double RPI = wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
			printf("%.6lf\n", RPI);
		}
	}
	return 0;
}
