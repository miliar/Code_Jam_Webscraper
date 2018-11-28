//	GCJ 2010 Qual (C)

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
typedef pair<int,int> pint;
#define mp make_pair

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
int in_c() { int c; for (; (c = getchar()) <= ' '; ) { if (!~c) throw ~0; } return c; }
int in() {
	int x = 0, c;
	for (; (uint)((c = getchar()) - '0') >= 10; ) { if (c == '-') return -in(); if (!~c) throw ~0; }
	do { x = (x << 3) + (x << 1) + (c - '0'); } while ((uint)((c = getchar()) - '0') < 10);
	return x;
}

const int E = 30;

int R, N;
Int K, G[1010];
Int sum[2010];

int to[40][1010];
Int euro[40][1010];

int main() {
	int i, j, e;
	
	for (int TC = in(), tc = 0; ++tc <= TC; ) {
		R = in();
		K = in();
		N = in();
		for (i = 0; i < N; ++i) {
			G[i] = in();
		}
		for (i = 0; i < N + N; ++i) {
			sum[i + 1] = sum[i] + G[i % N];
		}
		for (i = 0; i < N; ++i) {
			j = upper_bound(sum + i, sum + i + N + 1, sum[i] + K) - sum - 1;
			to[0][i] = j % N;
			euro[0][i] = sum[j] - sum[i];
		}
		for (e = 0; e < E; ++e) {
			for (i = 0; i < N; ++i) {
				to[e + 1][i] = to[e][ to[e][i] ];
				euro[e + 1][i] = euro[e][i] + euro[e][ to[e][i] ];
			}
		}
		Int ans = 0;
		for (i = 0, e = 0; e < E; ++e) if (R & 1 << e) {
			ans += euro[e][i];
			i = to[e][i];
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	
	return 0;
}

