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

#define MAX 128

int r;
bool map[MAX][MAX];

void reset() {
	REP(i, MAX) {
		REP(j, MAX) {
			map[i][j] = false;
		}
	}
}

void read_input() {
	int x1, y1, x2, y2;
	scanf("%d", &r);
	REP(i, r) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		FOR(x, x1, x2) {
			FOR(y, y1, y2) {
				map[x][y] = true;
			}
		}
	}
}

bool all_die() {
	REP(i, MAX) {
		REP(j, MAX) {
			if(map[i][j])
				return false;
		}
	}
	return true;
}

bool die(int x, int y) {
	if(x < 0 || y < 0)return true;
	return !map[x][y];
}

void cal() {
	RFOR(x, MAX - 1, 0) {
		RFOR(y, MAX - 1, 0) {
			if(die(x - 1, y) && die(x, y - 1)) {
				map[x][y] = false;
			}
			if(!die(x - 1, y) && !die(x, y - 1)) {
				map[x][y] = true;
			}
		}
	}
}

void print() {
	printf("\n");
	REP(i, MAX) {
		REP(j, MAX) {
			if(map[i][j])
				printf("1");
			else printf("0");
		}
		printf("\n");
	}
}

void find_ans() {
	reset();
	read_input();
	//print();

	int ans = 0;
	while(!all_die()) {
		cal();
		//print();
		ans++;
	}

	printf("%d", ans);
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
