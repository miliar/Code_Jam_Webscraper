#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define NEED_BIG_INT 0
#define DEBUG_FLAG 1

#if NEED_BIG_INT
#include <gmpxx.h>
typedef mpz_class bint;
typedef mpq_class brational;
typedef mpf_class bdecimal;
// compile with -lgmpxx -lgmp (may need -lm too)
#endif

#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

const int OFF = 512;
int N;
int a[1024][1024];

inline int A(int x, int y) {
	return a[OFF+x][OFF+y];
}

int can(int x, int y) {
	for (int i = -N+1; i <= N-1; ++i)
		for (int j = -(N-abs(i)-1); j <= N-abs(i)-1; ++j)
			if (A(i, j) != -1) {
				if (A(x+x-i, y+y-j) != -1 && A(x+x-i, y+y-j) != A(i, j))
					return 1000000;
				else if (A(i, y+y-j) != -1 && A(i, y+y-j) != A(i, j))
					return 1000000;
				else if (A(x+x-i, j) != -1 && A(x+x-i, j) != A(i, j))
					return 1000000;
			}
	return (abs(x)+abs(y)+N)*(abs(x)+abs(y)+N)-N*N;
}

int main() {
	//string fname = "A-small-attempt1";
	string fname = "A-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		memset(a, -1, sizeof(a));
		scanf("%d", &N);
		for (int i = -N+1; i <= N-1; ++i)
			for (int j = -(N-abs(i)-1); j <= N-abs(i)-1; ++j) {
				if (j > -(N-abs(i)-1)) a[OFF+i][OFF+j++] = 5000;
				scanf("%d", &a[OFF+i][OFF+j]);
			}
		int r = 1000000;
		for (int i = -64; i <= 64; ++i)
			for (int j = -64; j <= 64; ++j)
				r = min(r, can(i, j));
		printf("Case #%d: %d\n", CASE, r);
	}

	return 0;
}
