#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

int T[100][100][2];

void testcase(int v) {
	printf("Case #%d: ", v);
	REP(i,100) REP(j,100) T[i][j][0] = T[i][j][1] = 0;
	int r;
	scanf("%d", &r);
	REP(i,r) {
		int x1, x2, y1, y2;
		scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
		--y1; --x1; --x2; --y2;
		if(x1 > x2) swap(x1,x2);
		if(y1 > y2) swap(y1,y2);
		FOR(i,x1,x2) FOR(j,y1,y2)
			T[i][j][0] = 1;
	}
	int result = 0;
	for(;;) {
		bool end = true;
		REP(i,100) REP(j,100) if(T[i][j][0]) { end = false; break; }
		if(end) break;
		++result;
		REP(i,100) REP(j,100) T[i][j][1] = T[i][j][0];
		REP(i,100) REP(j,100) T[i][j][0] = 0;
		bool gora, lewo;
		REP(i,100) REP(j,100) {
			gora = ((i != 0) && T[i-1][j][1] != 0);
			lewo = ((j != 0) && T[i][j-1][1] != 0);
			T[i][j][0] = T[i][j][1];
			if( !gora && !lewo) T[i][j][0] = 0;
			else if(gora && lewo) T[i][j][0] = 1;
		}
	}
	printf("%d\n", result);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

