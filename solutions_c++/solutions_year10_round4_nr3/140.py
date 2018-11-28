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

typedef pair<int, int> pii;

const int S = 128;
int N;
bool a[S][S];
bool next[S][S];

int f() {
	bool flag = false;
	memset(next, false, sizeof(next));
	for (int i = 0; i < S-1; ++i)
		for (int j = 0; j < S-1; ++j) {
			if (a[i][j]) {
				flag = true;
				if ((i > 0 && a[i-1][j]) || (j > 0 && a[i][j-1])) next[i][j] = true;
			}
			if (!a[i+1][j+1] && a[i+1][j] && a[i][j+1])
				next[i+1][j+1] = true;
		}
	memcpy(a, next, sizeof(a));
	if (!flag) return 0;
	else return 1+f();
}

int main() {
	string fname = "C-small-attempt0";
	//string fname = "C-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		memset(a, false, sizeof(a));
		scanf("%d", &N);
		for (int k = 0; k < N; ++k) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; ++i)
				for (int j = y1; j <= y2; ++j)
					a[i][j] = true;
		}
		printf("Case #%d: %d\n", CASE, f());
	}

	return 0;
}
