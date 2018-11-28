#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
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
#define cdbg(...)
#define dbg(...)
#endif

int D, L, B, K;
int p[1000000], pn = 0;
bool a[1000000];
int s[16];

long long mult_inverse (long long n, long long p)
{
    long long r = 1, e = p-2;
    do {if (e&1) r=(r*n)%p; n=(n*n)%p;} while (e>>=1);
    return r;
}

int f() {
	int ans = -1;
	for (int k = 0; k < pn; ++k) {
		long long P = p[k];
		if (P < B || P > L) continue;
		if (s[0] == s[1]) return s[0];
		else if (K <= 2) return -1;
		long long A = ((s[2] - s[1] + P) * mult_inverse(s[1] - s[0] + P, P)) % P;
		long long B = (s[1] - A * s[0] + P * P) % P;
		bool can = true;
		for (int i = 1; i < K; ++i)
			if (s[i] != (A*s[i-1] + B) % P) can = false;
		if (can) {
			int ca = (A*s[K-1] + B) % P;
			if (ans != -1 && ca != ans) return -1;
			ans = ca;
		}
	}
	return ans;
}

int main() {
	//string fname = "A-small-attempt0";
	string fname = "A-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	memset (a, true, sizeof(a));
	for (int i = 2; i < 1000000; ++i)
		if (a[i])
			for (int j = i+i; j < 1000000; j += i)
				a[j] = false;
	for (int i = 2; i < 1000000; ++i)
		if (a[i])
			p[pn++] = i;
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		scanf("%d%d", &D, &K);
		L = 1; B = 0;
		for (int i = 0; i < D; ++i) L *= 10;
		for (int i = 0; i < K; ++i) {
			scanf("%d", &s[i]);
			B = max(B, s[i]+1);
		}
		int ans = f();
		if (ans != -1)
			printf("Case #%d: %d\n", CASE, ans);
		else
			printf("Case #%d: I don't know.\n", CASE);
	}

	return 0;
}
