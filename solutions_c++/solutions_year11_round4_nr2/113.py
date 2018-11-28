#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define ALL(a) (a).begin(),(a).end()
#define PB(a) push_back(a)
#define MP(a,b) make_pair((a),(b))
#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}

const int N = 511;

long long getSum(long long SUM[N][N], int x, int y) {
	if (x < 0 || y < 0) {
		return 0;
	}
	return SUM[x][y];
}

long long getSum(long long SUM[N][N], long long VAL[N][N], int x1, int y1, int x2, int y2) {
	long long res = getSum(SUM, x2, y2) - getSum(SUM, x1 - 1, y2) - getSum(SUM, x2, y1 - 1) + getSum(SUM, x1 - 1, y1 - 1);
	res -= VAL[x1][y1] + VAL[x1][y2] + VAL[x2][y1] + VAL[x2][y2];
	return res;
}

long long SUM[N][N], XSUM[N][N], YSUM[N][N];
long long VAL[N][N], XVAL[N][N], YVAL[N][N];


int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int R = nextInt();
		int C = nextInt();
		long long D = nextInt();
		vector<string> field(R);
		for (int i = 0; i < R; ++i) {
			field[i] = nextString();
		}
		long long mx = 0;
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				SUM[i][j] = VAL[i][j] = D + field[i][j] - '0';
				if (i - 1 >= 0) SUM[i][j] += SUM[i - 1][j];
				if (j - 1 >= 0) SUM[i][j] += SUM[i][j - 1];
				if (i - 1 >= 0 && j - 1 >= 0) SUM[i][j] -= SUM[i - 1][j - 1];

				XSUM[i][j] = XVAL[i][j] = i * (D + field[i][j] - '0');
				if (i - 1 >= 0) XSUM[i][j] += XSUM[i - 1][j];
				if (j - 1 >= 0) XSUM[i][j] += XSUM[i][j - 1];
				if (i - 1 >= 0 && j - 1 >= 0) XSUM[i][j] -= XSUM[i - 1][j - 1];

				YSUM[i][j] = YVAL[i][j] = j * (D + field[i][j] - '0');
				if (i - 1 >= 0) YSUM[i][j] += YSUM[i - 1][j];
				if (j - 1 >= 0) YSUM[i][j] += YSUM[i][j - 1];
				if (i - 1 >= 0 && j - 1 >= 0) YSUM[i][j] -= YSUM[i - 1][j - 1];
			}
		}
		int res = 0;
		for (int k = min(R, C); k >= 3; --k) {
			for (int i = 0; i + k <= R; ++i) {
				for (int j = 0; j + k <= C; ++j) {
					long long s = getSum(SUM, VAL, i, j, i + k - 1, j + k - 1);
					long long sx = getSum(XSUM, XVAL, i, j, i + k - 1, j + k - 1);
					long long sy = getSum(YSUM, YVAL, i, j, i + k - 1, j + k - 1);
					mx = max(mx, s);
					mx = max(mx, sx);
					mx = max(mx, sy);
					if ((sx * 2 == s * (i + i + k - 1)) && (sy * 2 == s * (j + j + k - 1))) {
						res = k;
					}
				}
			}
			if (res > 0) {
				break;
			}
		}
		//cerr << mx << endl;
		cerr << cas << endl;
		printf("Case #%d: ", cas);
		if (res == 0) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", res);
		}
	}
	return 0;
}
