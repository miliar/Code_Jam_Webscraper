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

int a[200][200];
int u[1 << 20];
int d[1 << 20];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		memset(u, 0, sizeof(u));
		int result = 0;
		int n, k; scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < k; ++j) {
				scanf("%d", &a[i][j]);
			}
		}
		u[0] = true;
		for (int i = 1; i < 1 << n; ++i) {
			int t = 0;
			while ((t < n) && !(i & (1 << t))) {
				++t;
			}
			if (!u[i ^ (1 << t)]) continue;
			u[i] = true;
			for (int j = t + 1; j < n; ++j) if (i & (1 << j)) {
				bool f1 = false, f2 = false;
				for (int l = 0; l < k; ++l) {
					if (a[t][l] < a[j][l]) f1 = true;
					else if (a[t][l] > a[j][l]) f2 = true;
					else f1 = f2 = true;
				}
				if (f1 && f2) {
					u[i] = false;
					break;
				}
			}
		}
		
		memset(d, ~0, sizeof(d));
		d[0] = 0;
		for (int i = 1; i < 1 << n; ++i) {
			if (u[i]) d[i] = 1;
			else for (int j = i; j > 0; j = (j - 1) & i) {
				if (u[j] && (d[i ^ j] != -1) && ((d[i] == -1) || (d[i] > d[i ^ j] + 1))) {
					d[i] = d[i ^ j] + 1;
				}
			}
		}
		
		
//		u[0] = 0;
/*		for (int i = 1; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				bool f1 = false, f2 = false;
				for (int t = 0; t < k; ++t) {
					if (a[i][t] < a[j][t]) f1 = true;
					else if (a[i][t] > a[j][t]) f2 = true;
					else f1 = f2 = true;
				}
				if (f1 && f2) continue;
			}
		}*/
		printf("Case #%d: %d\n", tt + 1, d[(1 << n) - 1]);
	}
	return 0;
}
