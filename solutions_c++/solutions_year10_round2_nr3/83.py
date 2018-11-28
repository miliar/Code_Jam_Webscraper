// includes + defines {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define FORD(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int)((x).size()))
#define DEBUG(x) { cout << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;
// }}}

#define MOD 100003
#define MAXN 507
typedef long long LL;

#define add(x, y) (((x) + (y)) % MOD)
#define mul(x, y) (((LL)(x) * (LL)(y)) % MOD)

int _C[MAXN][MAXN];

void init_C(){
	FOR(i, 0, MAXN - 1){
		_C[i][0] = _C[i][i] = 1;

		FOR(j, 1, i - 1)
			_C[i][j] = add(_C[i - 1][j - 1], _C[i - 1][j]);
	}
}

int C(int n, int k){
	if(n < 0 || k < 0 || k > n)
		return 0;

	return _C[n][k];
}

int main(){
	init_C();
	int T;
	cin >> T;
	FOR(qi, 1, T){
		int N;
		cin >> N;

		vector<vector<int> > D(N + 1, vector<int>(N, 0));

		FOR(i, 2, N){
			D[i][1] = 1;

			FOR(j, 2, i - 1)
				FOR(k, 0, j - 2)
					D[i][j] = add(D[i][j], mul(D[j][j - 1 - k], C(i - j - 1, k)));
		}

		int res = 0;
		FOR(j, 1, N - 1)
			res = add(res, D[N][j]);

		cout << "Case #" << qi << ": " << res << endl;
	}
}
