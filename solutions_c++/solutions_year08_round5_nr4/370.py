#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <time.h>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

#define N 105
#define inr(i,j) (0 <= i && i < n && 0 <= j && j < m)
#define M 10007

int a[N][N], n, m, r;

int main () {
	int i, j, x, y, ii, jj, T;

	scanf("%d", &T);

	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d%d", &n, &m, &r);

		mset(a,0);

		for (i = 0; i < r; i++) {
			scanf("%d%d", &x, &y);
			x--; y--;
			a[x][y] = -1;
		}

		a[0][0] = 1;

		for (i = 0; i < n; i++) for (j = 0; j < m; j++) if (a[i][j] > 0) {
			ii = i+1, jj = j+2;
			if (inr(ii,jj) && a[ii][jj] != -1) a[ii][jj] += a[i][j], a[ii][jj] %= M;
			ii = i+2, jj = j+1;
			if (inr(ii,jj) && a[ii][jj] != -1) a[ii][jj] += a[i][j], a[ii][jj] %= M;
		}
		
		printf("Case #%d: %d\n", cas, a[n-1][m-1]);
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}
