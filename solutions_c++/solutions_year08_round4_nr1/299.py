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

#define N 10111
#define INF 1000000000

#define L(x) ( ((x)<<1)+1 )
#define R(x) ( ((x)<<1)+2 )

int value[N];
int oper[N];
int ch[N];
int m, V;
int dp[N][2];

inline int f(int v, int b) {
	if (dp[v][b] != -1) {
		return dp[v][b];
	}
	if (v >= (m-1)/2) {
		if (b == value[v]) return 0;
		return INF;
	}
	int res = INF;

	if (oper[v]) {
		if (b == 0) {
			res = min( res, f( L(v), 0 ) + f( R(v), 0 )  );
			res = min( res, f( L(v), 0 ) + f( R(v), 1 )  );
			res = min( res, f( L(v), 1 ) + f( R(v), 0 )  );
		}
		else {
			res = min( res, f( L(v), 1 ) + f( R(v), 1 ) );
		}
	}
	else {
		if (b == 0) {
			res = min( res, f( L(v), 0 ) + f( R(v), 0 )  );
		}
		else {
			res = min( res, f( L(v), 0 ) + f( R(v), 1 )  );
			res = min( res, f( L(v), 1 ) + f( R(v), 0 )  );
			res = min( res, f( L(v), 1 ) + f( R(v), 1 )  );
		}
	}

	if (ch[v]) {
		if (oper[v] == 0) {
			if (b == 0) {
				res = min( res, f( L(v), 0 ) + f( R(v), 0 ) + 1 );
				res = min( res, f( L(v), 0 ) + f( R(v), 1 ) + 1 );
				res = min( res, f( L(v), 1 ) + f( R(v), 0 ) + 1 );
			}
			else {
				res = min( res, f( L(v), 1 ) + f( R(v), 1 ) + 1 );
			}
		}
		else {
			if (b == 0) {
				res = min( res, f( L(v), 0 ) + f( R(v), 0 ) + 1 );
			}
			else {
				res = min( res, f( L(v), 0 ) + f( R(v), 1 ) + 1 );
				res = min( res, f( L(v), 1 ) + f( R(v), 0 ) + 1 );
				res = min( res, f( L(v), 1 ) + f( R(v), 1 ) + 1 );
			}
		}
	}

	return dp[v][b] = res;
}


int main () {
	int i, j, T;

	scanf("%d", &T);
	
	for (int cas = 1; cas <= T; cas++) {

		scanf("%d%d", &m, &V);

		for (i = 0; i < (m-1)/2; i++) scanf("%d%d", &oper[i], &ch[i]);
		for (i = (m-1)/2; i < m; i++) scanf("%d", &value[i]);

		mset(dp, -1);

		int res = f( 0, V );

		printf("Case #%d:", cas);

		if (res >= INF) printf(" IMPOSSIBLE\n");
		else printf(" %d\n", res);

		cerr << cas << "\n";
	}

	return 0;
}

