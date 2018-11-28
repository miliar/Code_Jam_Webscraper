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

#define MAX 1024
#define N 4

char _map[MAX][MAX];

void reset() {

}

void read_input() {
	REP(i, N) {
		scanf("%s", _map[i]);
	}
}

char check(int sx, int sy, int ax, int ay) {
	char ch = 0;
	REP(i, N) {
		char tmp = _map[sx + ax * i][sy + ay * i];
		if(tmp == 'T')continue;
		if(tmp == '.')return 0;
		if(!ch)ch = tmp;
		if(ch != tmp)return 0;
	}
	return ch;
}

void find_ans() {
	read_input();

	char ch;
	REP(i, N) {
		ch = check(i, 0, 0, 1);
		if(ch) {
			printf("%c won", ch);
			return;
		}
		ch = check(0, i, 1, 0);
		if(ch) {
			printf("%c won", ch);
			return;
		}
	}
	ch = check(0, 0, 1, 1);
	if(ch) {
		printf("%c won", ch);
		return;
	}
	ch = check(0, N - 1, 1, -1);
	if(ch) {
		printf("%c won", ch);
		return;
	}

	REP(i, N) {
		REP(j, N) {
			if(_map[i][j] == '.') {
				printf("Game has not completed");
				return;
			}
		}
	}

	printf("Draw");
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
