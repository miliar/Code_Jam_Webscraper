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

const int N = 1000000;
int b[N+1], e[N+1];

int main() {
	//string fname = "C-small-attempt0";
	string fname = "C-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);

	for (int i = 1; i <= N; ++i) b[i] = e[i] = i;
	for (int i = 1, x = 2; i <= N; ++i) {
		e[i] = min(N, b[i] + i - 1);
		for (; x <= e[i]; ++x)
			b[x] = i;
	}

	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		int A1, A2, B1, B2;
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		long long r = 0;
		for (int i = A1; i <= A2; ++i)
			r += max(0, min(e[i], B2) - max(B1, b[i]) + 1);
		r = (long long) (A2-A1+1) * (long long)(B2-B1+1) - r;
		printf("Case #%d: %lld\n", CASE, r);
	}

	return 0;
}
