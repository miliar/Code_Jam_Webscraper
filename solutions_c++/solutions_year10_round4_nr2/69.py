//	GCJ 2010 Round 2 (B)

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef vector<int> vint;
typedef vector<string> vstr;
typedef pair<int,int> pint;
#define mp make_pair

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<class T> void pvp(T a, T b) { for (T i = a; i != b; ++i) cout << "(" << i->first << ", " << i->second << ") "; cout << endl; }
void chmin(int &t, int f) { if (t > f) t = f; }
void chmax(int &t, int f) { if (t < f) t = f; }
void chmin(Int &t, Int f) { if (t > f) t = f; }
void chmax(Int &t, Int f) { if (t < f) t = f; }
void chmin(double &t, double f) { if (t > f) t = f; }
void chmax(double &t, double f) { if (t < f) t = f; }
int in_c() { int c; for (; (c = getchar()) <= ' '; ) { if (!~c) throw ~0; } return c; }
int in() { int x = 0, c; for (; (uint)((c = getchar()) - '0') >= 10; ) { if (c == '-') return -in(); if (!~c) throw ~0; } do { x = (x << 3) + (x << 1) + (c - '0'); } while ((uint)((c = getchar()) - '0') < 10); return x; }
Int In() { Int x = 0, c; for (; (uint)((c = getchar()) - '0') >= 10; ) { if (c == '-') return -In(); if (!~c) throw ~0; } do { x = (x << 3) + (x << 1) + (c - '0'); } while ((uint)((c = getchar()) - '0') < 10); return x; }

const int INF = 1001001001;

int P, N;
int M[1030];
int C[20][1030];
int dp[20][1030][20];

int main() {
	int i, j;
	int p;
	
	for (int TC = in(), tc = 0; ++tc <= TC; ) {
		P = in();
		N = 1 << P;
		for (i = 0; i < N; ++i) {
			M[i] = in();
		}
		for (p = 1; p <= P; ++p) {
			for (i = 0; i < N; i += 1 << p) {
				C[p][i] = in();
			}
		}
		memset(dp, 0x3f, sizeof(dp));
		
		for (i = 0; i < N; ++i) {
			for (j = 0; j <= M[i]; ++j) {
				dp[0][i][j] = 0;
			}
		}
		for (p = 1; p <= P; ++p) {
			for (i = 0; i < N; i += 1 << p) {
				for (j = 0; j <= P; ++j) {
					chmin(dp[p][i][j], C[p][i] + dp[p - 1][i][j] + dp[p - 1][i | (1 << p - 1)][j]);
					chmin(dp[p][i][j], dp[p - 1][i][j + 1] + dp[p - 1][i | (1 << p - 1)][j + 1]);
				}
			}
		}
		int res = dp[P][0][0];
		printf("Case #%d: %d\n", tc, res);
	}
	
	return 0;
}

