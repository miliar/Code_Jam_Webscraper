#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define pb push_back
#define mp make_pair

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? (-(x)) : (x))

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

char p[10000];
char w[10000][1000];
int c[1000][26];
int e[26];
int f[26];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int k;
		scanf("%s %d", p, &k);
		int n; scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", w[i]);
			for (int j = 0; j < 26; ++j) {
				c[i][j] = 0;
			}
			for (int j = 0; w[i][j]; ++j) {
				++c[i][w[i][j] - 'a'];
			}
		}
		int d[100];
		for (int i = 1; i <= k; ++i) {
			d[i] = 0;
		}
		for (int K = 1; K <= k; ++K) {
			for (int i = 0; i < K; ++i) {
				f[i] = 0;
			}
			while (f[0] < n) {
				for (int j = 0; j < 26; ++j) {
					e[j] = 0;
				}
				for (int j = 0; j < K; ++j) {
					for (int k = 0; k < 26; ++k) {
						e[k] += c[f[j]][k];
					}
				}
				int s = 0;
				int pp = 1;
				for (int j = 0; p[j] != 0; ++j) {
					if (isalpha(p[j])) {
						pp *= e[p[j] - 'a'];
						pp %= 10009;
					} else {
						s += pp;
						pp = 1;
					}
				}
				s += pp;
				s %= 10009;
				d[K] = (d[K] + s) % 10009;
				++f[K - 1];
				for (int i = K - 1; i > 0; --i) {
					if (f[i] < n) break;
					f[i] = 0;
					++f[i - 1];
				}
			}
		}
/*		for (int i = 1; i < 1 << n; ++i) {
			int t = 0;
			for (int j = 0; j < n; ++j) if (i & (1 << j)) {
				++t;
			}
			if (t <= k) {
				for (int j = 0; j < 26; ++j) {
					e[j] = 0;
				}
				for (int j = 0; j < n; ++j) if (i & (1 << j)) {
					for (int k = 0; k < 26; ++k) {
						e[k] += c[j][k];
					}
				}
				int s = 0;
				int pp = 1;
				for (int j = 0; p[j] != 0; ++j) {
					if (isalpha(p[j])) {
						pp *= e[p[j] - 'a'];
//						pp %= 10009;
					} else {
						s += pp;
						pp = 1;
					}
				}
				s += pp;
//				s %= 10009;
				for (int j = 2; j <= t; ++j) {
					s = (s * j);// % 10009;
				}
				d[t] += s;
			}
		}*/
		printf("Case #%d:", tt + 1);
		for (int i = 1; i <= k; ++i) {
			printf(" %d", d[i]);
		}
		putchar('\n');
		fflush(stdout);
	}
	return 0;
}
