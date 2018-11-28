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

int main(){
	int T;
	scanf("%d", &T);
	FOR(qi, 1, T){
		int P;
		scanf("%d", &P);
		vector<int> C(1 << P);
		REP(i, 1 << P)
			scanf("%d", &C[i]);
		vector<vector<int> > L(P);
		REP(i, P){
			L[i].resize(1 << (P - 1 - i));
			REP(j, SIZE(L[i]))
				scanf("%d", &L[i][j]);
		}

		vector<vector<vector<int> > > D(P);
		D[0].resize(1 << (P - 1), vector<int>(P + 2, INF));
		REP(i, 1 << (P - 1)){
			D[0][i][min(C[2 * i], C[2 * i + 1])] = L[0][i];
			FORD(j, min(C[2 * i], C[2 * i + 1]) - 1, 0)
				D[0][i][j] = 0;
		}

		FOR(i, 1, P - 1){
			D[i].resize(1 << (P - 1 - i), vector<int>(P + 2, INF));
			REP(j, 1 << (P - 1 - i)) REP(k, P + 1)
				D[i][j][k] = min(D[i][j][k], min(
					L[i][j] + D[i - 1][2 * j][k] + D[i - 1][2 * j + 1][k],
					D[i - 1][2 * j][k + 1] + D[i - 1][2 * j + 1][k + 1]));
		}

		printf("Case #%d: %d\n", qi, D[P - 1][0][0]);
	}
}
