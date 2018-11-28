#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define debug(x) cout<<(#x)<<":"<<(x)<<endl

char a[10][10];

int main() {
	int tN;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		scanf("\n");
		REP(i, 4) gets(a[i]);
		bool winX = 0, winO = 0, dot = 0;
		REP(i, 4)
		REP(j, 4) if (a[i][j] == '.') dot = 1;
		REP(i, 4) {
			int cntX = 0, cntO = 0;
			REP(j, 4) if (a[i][j] == 'X' || a[i][j] == 'T') ++cntX;
			REP(j, 4) if (a[i][j] == 'O' || a[i][j] == 'T') ++cntO;
			if (cntX == 4) winX = 1;
			if (cntO == 4) winO = 1;
		}
		REP(j, 4) {
			int cntX = 0, cntO = 0;
			REP(i, 4) if (a[i][j] == 'X' || a[i][j] == 'T') ++cntX;
			REP(i, 4) if (a[i][j] == 'O' || a[i][j] == 'T') ++cntO;
			if (cntX == 4) winX = 1;
			if (cntO == 4) winO = 1;
		}
		REP(j, 1) {
			int cntX = 0, cntO = 0;
			REP(i, 4) if (a[i][i] == 'X' || a[i][i] == 'T') ++cntX;
			REP(i, 4) if (a[i][i] == 'O' || a[i][i] == 'T') ++cntO;
			if (cntX == 4) winX = 1;
			if (cntO == 4) winO = 1;
		}
		REP(j, 1) {
			int cntX = 0, cntO = 0;
			REP(i, 4) if (a[i][3-i] == 'X' || a[i][3-i] == 'T') ++cntX;
			REP(i, 4) if (a[i][3-i] == 'O' || a[i][3-i] == 'T') ++cntO;
			if (cntX == 4) winX = 1;
			if (cntO == 4) winO = 1;
		}
		printf("Case #%d: ", cN);
		if (winX) puts("X won");
		else if (winO) puts("O won");
		else if (dot) puts("Game has not completed");
		else puts("Draw");
	}
}
