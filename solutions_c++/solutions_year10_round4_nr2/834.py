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
#define MAXA 1024000000

int p, data[MAX][MAX], m[MAX];

void reset() {

}

void read_input() {
	scanf("%d", &p);
	REP(i, 1 << p) {
		scanf("%d", &m[i]);
		m[i] = p - m[i];
	}
	REP(i, p) {
		int k = 1 << (p - i - 1);
		REP(j, k) {
			scanf("%d", &data[i][j]);
		}
	}
}

int cal(int p, int x, int* m) {
	if(p < 0) {
		if(m[x] > 0)
			return MAXA;
		return 0;
	}

	bool pass = true;
	int s = x * (1 << (p + 1));
	int e = (x + 1) * (1 << (p + 1)) - 1;
	FOR(i, s, e) {
		if(m[i] > 0)
			pass = false;
	}
	if(pass) {
		return 0;
	}

	int tmp[MAX];
	FOR(i, s, e)
		tmp[i] = m[i] - 1;
	int al = cal(p - 1, x * 2, tmp);
	int ar = cal(p - 1, x * 2 + 1, tmp);
	int a = data[p][x] + al + ar;

	FOR(i, s, e)
		tmp[i] = m[i];
	int bl = cal(p - 1, x * 2, tmp);
	int br = cal(p - 1, x * 2 + 1, tmp);
	int b = bl + br;

	return min(a, b);
}

void find_ans() {
	read_input();

	int tmp[MAX];
	REP(i, MAX)
		tmp[i] = m[i];

	printf("%d", cal(p - 1, 0, tmp));
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
