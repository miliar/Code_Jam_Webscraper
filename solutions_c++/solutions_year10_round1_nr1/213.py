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

const int di[] = {1, 0, 1, 1}, dj[] = {0, 1, 1, -1};
int N, K;
char b[64][64];

bool f(char c) {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			for (int d = 0; d < 4; ++d) {
				bool can = true;
				for (int k = 0; k < K; ++k) {
					int ii = i+k*di[d], jj = j+k*dj[d];
					if (ii < 0 || ii >= N || jj < 0 || jj >= N || b[ii][jj] != c)
						can = false;
				}
				if (can) return true;
			}
	return false;
}

int main() {
	//string fname = "A-small-attempt0";
	string fname = "A-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; ++i)
			scanf("%s", b[i]);
		for (int i = 0; i < N; ++i) {
			int x = N-1;
			for (int j = N-1; j >= 0; --j)
				if (b[i][j] != '.')
					b[i][x--] = b[i][j];
			for (x; x >= 0; --x)
				b[i][x] = '.';
		}
		bool R = f('R'), B = f('B');
		if (B && R) printf("Case #%d: Both\n", CASE);
		if (!B && !R) printf("Case #%d: Neither\n", CASE);
		if (B && !R) printf("Case #%d: Blue\n", CASE);
		if (!B && R) printf("Case #%d: Red\n", CASE);
	}

	return 0;
}
