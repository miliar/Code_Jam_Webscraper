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

#define MAXN 150

char buf[MAXN], A[MAXN][MAXN];

#define dnu(x) ((0 <= (x)) && ((x) < M))

int main(){
	int T;
	scanf("%d ", &T);
	FOR(qi, 1, T){
		int N, M;
		fgets(buf, MAXN, stdin);
		sscanf(buf, "%d", &N);
		M = 2 * N - 1;
		REP(i, M)
			fgets(A[i], MAXN, stdin);
		REP(i, N) FOR(j, N + i, M - 1)
			A[i][j] = ' ';
		FORD(i, N - 2, 0) FOR(j, N + i, M - 1)
			A[M - 1 - i][j] = ' ';

		int res = INF;
		REP(i, M) REP(j, M){
			bool ok = true;
			REP(a, M) REP(b, M){
				int c = a, d = 2 * j - b;
				if(dnu(c) && dnu(d) &&
				   A[c][d] != ' ' && A[a][b] != ' ' &&
				   A[c][d] != A[a][b])
					ok = false;

				c = 2 * i - a, d = b;
				if(dnu(c) && dnu(d) &&
				   A[c][d] != ' ' && A[a][b] != ' ' &&
				   A[c][d] != A[a][b])
					ok = false;
			}

			if(ok)
				res = min(res, 1 + max(
					max(i + j - (N - 1), N + M - 2 - (i + j)),
					max(i - j + (N - 1), N - 1 - (i - j))));
		}

		printf("Case #%d: %d\n", qi, SQR(res) - SQR(N));
	}
}
