#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

#define MAX 64

int n, k;
char init[MAX][MAX], board[MAX][MAX];

void read_input() {
	scanf("%d %d", &n, &k);
	REP(i, n)
		scanf("%s", init[i]);
	RFOR(i, n - 1, 0) {
		int x = 0;
		RFOR(j, n - 1, 0) {
			if(init[i][j] != '.')
				board[n - (++x)][n - i - 1] = init[i][j];
		}
		while(x < n)
			board[n - (++x)][n - i - 1] = '.';
	}
}

bool win(char ch) {
	REP(i, n) {
		REP(j, n) {
			FOR(x, -1, 1) {
				FOR(y, -1, 1) {
					if(x == 0 && y == 0)continue;

					int z = 0;
					for(z = 0; z < k; z++) {
						int ii = i + z * x;
						int jj = j + z * y;
						if(ii < 0 || ii >= n)break;
						if(jj < 0 || jj >= n)break;
						if(board[ii][jj] != ch)break;
					}
					if(z == k) {
						//printf("\n%c %d %d %d %d\n", ch, i, j, x, y);
						return true;
					}
				}
			}
		}
	}
	return false;
}

void print() {
	printf("\n");
	REP(i, n)
		printf("%s\n", board[i]);
}

void find_ans() {
	read_input();
	//print();
	bool r_win = win('R');
	bool b_win = win('B');
	if(r_win && b_win)
		printf("Both");
	else if(r_win)
		printf("Red");
	else if(b_win)
		printf("Blue");
	else printf("Neither");
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
