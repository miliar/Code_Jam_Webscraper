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
#define MAX_INT 2147483647

int n, c[MAX];

void read_input() {
	scanf("%d", &n);
	REP(i, n)
		scanf("%d", &c[i]);
}

void find_ans() {
	read_input();

	int sum = 0, bsum = 0, _min = MAX_INT;
	REP(i, n) {
		sum += c[i];
		bsum ^= c[i];
		REMIN(_min, c[i]);
	}
	if(bsum != 0) {
		printf("NO");
	} else {
		printf("%d", sum - _min);
	}
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
