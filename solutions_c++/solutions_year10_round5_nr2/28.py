//	GCJ 2010 Round 3 (B)

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

const int LIM = 10005;
const int INF = 1001001001;

Int L;
int N;
int B[110];
int dp[10010];

int main() {
	int i, j;
	
	for (int TC = in(), tc = 0; ++tc <= TC; ) {
		L = In();
		N = in();
		for (i = 0; i < N; ++i) {
			B[i] = in();
		}
		sort(B, B + N);
		memset(dp, 0x3f, sizeof(dp));
		dp[0] = 0;
		for (i = 0; i < N; ++i) {
			for (j = B[i]; j <= LIM; ++j) {
				chmin(dp[j], dp[j - B[i]] + 1);
			}
		}
		Int tmp = (L - LIM) / B[N - 1] + 1;
		L -= B[N - 1] * tmp;
		printf("Case #%d: ", tc);
		if (dp[L] < INF) {
			printf("%lld\n", tmp + dp[L]);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	
	return 0;
}

