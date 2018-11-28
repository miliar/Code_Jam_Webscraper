
#include <map>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <assert.h>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INPUT_FILE_NAME "A-large"
#define OUTPUT_FILE_NAME "a"

void solveCase() {
	int xRows[4] = {0, 0, 0, 0};
	int oRows[4] = {0, 0, 0, 0};
	int xCols[4] = {0, 0, 0, 0};
	int oCols[4] = {0, 0, 0, 0};
	int xDiag[2] = {0, 0};
	int oDiag[2] = {0, 0};
	int empty = 0;
	REP(i, 4) {
		char line[10];
		scanf("%s", line);
		REP(j, 4) {
			switch(line[j]) {
			case 'X':
				xRows[i] ++;
				xCols[j] ++;
				if(i==j) {
					xDiag[0] ++;
				}
				if(i+j == 3) {
					xDiag[1] ++;
				}
				break;
			case 'O':
				oRows[i] ++;
				oCols[j] ++;
				if(i==j) {
					oDiag[0] ++;
				}
				if(i+j == 3) {
					oDiag[1] ++;
				}
				break;
			case 'T':
				xRows[i] ++;
				oRows[i] ++;
				xCols[j] ++;
				oCols[j] ++;
				if(i==j) {
					xDiag[0] ++;
				}
				if(i==j) {
					oDiag[0] ++;
				}
				if(i+j == 3) {
					xDiag[1] ++;
				}
				if(i+j == 3) {
					oDiag[1] ++;
				}
				break;
			case '.':
				empty ++;
				break;
			default:
				assert(false);
				break;
			}
		}
	}
	REP(i, 4) {
		if(xRows[i] == 4 || xCols[i] == 4) {
			printf("%s", "X won");
			return;
		}
		if(oRows[i] == 4 || oCols[i] == 4) {
			printf("%s", "O won");
			return;
		}
	}
	REP(i, 2) {
		if(xDiag[0] == 4 || xDiag[1] == 4) {
			printf("%s", "X won");
			return;
		}
		if(oDiag[0] == 4 || oDiag[1] == 4) {
			printf("%s", "O won");
			return;
		}
	}
	if(empty == 0) {
		printf("%s", "Draw");
		return;
	}
	printf("%s", "Game has not completed");
	return;
}

int main() {
	freopen(INPUT_FILE_NAME ".in","r",stdin);
	freopen(OUTPUT_FILE_NAME ".out","w",stdout);
	int caseAmount;
	scanf("%d", &caseAmount);
	for (int caseNumber = 1; caseNumber <= caseAmount; ++caseNumber) {
		printf("Case #%d: ", caseNumber);
		solveCase();
		printf("\n");
	}
	return 0;
}
