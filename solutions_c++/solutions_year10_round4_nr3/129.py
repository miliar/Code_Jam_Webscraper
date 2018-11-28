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

#define MAXS 1007
bool G[MAXS][MAXS];

int main(){
	int T;
	scanf("%d", &T);
	FOR(qi, 1, T){
		cerr << qi << endl;
		int N;
		scanf("%d", &N);
		REP(i, MAXS) REP(j, MAXS)
			G[i][j] = false;
		while(N--){
			int X1, Y1, X2, Y2;
			scanf("%d %d %d %d", &X1, &Y1, &X2, &Y2);
			FOR(x, X1, X2) FOR(y, Y1, Y2)
				G[y][x] = true;
		}

		int res = 0;
		for(;;){
			bool any = false;
			REP(i, MAXS) REP(j, MAXS)
				if(G[i][j])
					any = true;
			if(!any)
				break;
			++res;

			FORD(u, 2 * (MAXS - 1), 0)
				FOR(y, 1, MAXS - 1){
					int x = u - y;
					if(0 < x && x < MAXS){
						if(G[y][x]){
							if(!G[y - 1][x] && !G[y][x - 1])
								G[y][x] = false;
						}else
							if(G[y - 1][x] && G[y][x - 1])
								G[y][x] = true;
					}
				}
		}

		printf("Case #%d: %d\n", qi, res);
	}
}
