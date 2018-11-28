#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;


int n, m;
int adjmask[9][9], a[9][9];
int midrow;


int nb(int i, int j) {
	return 1 << (i * m + j);
}

inline int cnt(int x) {
	int r = 0;
	while (x) {
		if (x % 2) r++;
		x /= 2;
	}
	return r;
}

void solvecase() {
	scanf("%d%d", &n, &m);
	FOR(i, n) FOR(j, m) scanf("%d", &a[i][j]);
	FOR(i, n) FOR(j, m) {
		adjmask[i][j] = 0;
		for (int di = -1; di <= 1; di++)
			for (int dj = -1; dj <= 1; dj++) {
				int ii = i + di;
				int jj = j + dj;
				if (ii >= 0 && jj >= 0 && ii < n && jj < m) adjmask[i][j] |= nb(ii, jj);
			}
	}
	midrow = 0;
	FOR(i, m) midrow |= nb(n/2, i);
	int N = 1<<(n*m);
	int res = 0;
	FOR(mask, N) {
		bool ok = true;
		FOR(i, n) {
			FOR(j, m) if (cnt(mask & adjmask[i][j]) != a[i][j]) { ok = false; break; }
			if (!ok) break;
		}
		if (ok) {
			res = max(res, cnt(mask & midrow));
		}
	}
	printf("%d", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}