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

void move(int *ans, int *pp, int *tt, int p) {
	*tt = max(*ans, *tt + abs(*pp - p)) + 1;
	*pp = p;
	REMAX(*ans, *tt);
}

void find_ans() {
	int n, ans = 0, bp = 1, bt = 0, op = 1, ot = 0;
	scanf("%d", &n);

	char str[MAX];
	int p;
	REP(i, n) {
		scanf("%s %d", str, &p);
		if(str[0] == 'B') {
			move(&ans, &bp, &bt, p);
		} else {
			move(&ans, &op, &ot, p);
		}
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
