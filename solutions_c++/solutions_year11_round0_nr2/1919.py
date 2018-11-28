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

#define MAX 128

int C, D, n, l;
char c[MAX][MAX], d[MAX][MAX], str[MAX], ans[MAX];

void read_input() {
	scanf("%d", &C);
	REP(i, C)
		scanf("%s", c[i]);
	scanf("%d", &D);
	REP(i, D)
		scanf("%s", d[i]);
	scanf("%d", &n);
	scanf("%s", str);
}

bool combine() {
	REP(j, C)
		while(l > 1 && ((ans[l - 1] == c[j][0] && ans[l - 2] == c[j][1]) || (ans[l - 1] == c[j][1] && ans[l - 2] == c[j][0]))) {
			ans[--l - 1] = c[j][2];
			return true;
		}
	return false;
}

bool opposed() {
	REP(j, D)
		REP(x, l) {
			int y = l - 1;
			if((ans[x] == d[j][0] && ans[y] == d[j][1]) || (ans[x] == d[j][1] && ans[y] == d[j][0])) {
				l = 0;
				return true;
			}
		}
	return false;
}

void display() {
	printf("[");
	REP(i, l) {
		if(i > 0)printf(", ");
		printf("%c", ans[i]);
	}
	printf("]");
}

void find_ans() {
	read_input();

	l = 0;
	REP(i, n) {
		ans[l++] = str[i];
		combine();
		opposed();
	}
	display();
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
