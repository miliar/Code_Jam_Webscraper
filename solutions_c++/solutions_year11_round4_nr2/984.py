#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)
#define FI first
#define SE second

#define PROBLEM "B"

const int MAXN = 512;
const double EPS = 1e-9;

int a[MAXN][MAXN];
int n, m, d;

bool okcenter(int i0, int j0, int s) {
	int i1 = i0 + s, j1 = j0 + s;
	assert(i1 <= n && j1 <= m);

	double ci = i0 + double (i1 - i0) / 2, cj = j0 + double (j1 - j0) / 2;
	double sumi = 0, sumj = 0;

    for (int i = i0; i < i1; i++) {
    	for (int j = j0; j < j1; j++) {
    		if ((i == i0 || i == i1-1) && (j == j0 || j == j1-1)) continue;
			
			double x = i + 0.5, y = j + 0.5;
            sumi += (x - ci) * a[i][j];
            sumj += (y - cj) * a[i][j];
    	}
    }

    //if (s == 5) cerr << i0 << " " << j0  << " " << i1 << " " << j1 << " " << ci << " " << cj << " " << sumi << " " << sumj << endl;
    return (fabs(sumi) < EPS && fabs(sumj) < EPS);
}

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		memset(a, 0, sizeof(a));

		scanf("%d %d %d", &n, &m, &d);

		for (int i = 0; i < n; i++) {
			scanf("\n");
			for (int j = 0; j < m; j++) {
				char c;
				scanf("%c", &c);
				assert('0' <= c && c <= '9');

				a[i][j] = d + (c - '0');
			}
		}

		int maxs = min(n, m);
		int found = -1;

		for (int s = maxs; s >= 3; s--) {
			for (int i = 0; i+s-1 < n; i++) {
				for (int j = 0; j+s-1 < m; j++) {
					if (okcenter(i, j, s)) {
						found = s;
						break;
					}
				}
				if (found != -1) break;
			}
			if (found != -1) break;
		}

		if (found != -1) printf("%d", found);
		else printf("IMPOSSIBLE");

		printf("\n");
	}

	return 0;
}
