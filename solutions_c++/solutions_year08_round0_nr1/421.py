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
#include <cmath>

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

#define N 111
#define M 1111
#define INF 1000000000

string s[N], q[M];
int dp[N][M];
int sn, qn;

inline int f(int x, int y) {
	if (dp[x][y] != -1) return dp[x][y];
	if (y == qn) return dp[x][y] = 0;
	int res = INF;
	for (int i = 0; i < sn; i++) if (s[i] != q[y]) res = min(res, f(i,y+1) + (i != x));
	return dp[x][y] = res;
}

int main () {
	int i, j, T;
	char str[111];

	gets(str); sscanf(str, "%d", &T);

	for (int cas = 1; cas <= T; cas++) {
		mset(dp,-1);
		
		gets(str); sscanf(str, "%d", &sn);
		for (i = 0; i < sn; i++) gets(str), s[i] = str;

		gets(str); sscanf(str, "%d", &qn);
		for (i = 0; i < qn; i++) gets(str), q[i] = str;

		int res = INF;
		for (i = 0; i < sn; i++) res = min(res, f(i,0));
		
		printf("Case #%d: %d\n", cas, res);
	}

	return 0;
}