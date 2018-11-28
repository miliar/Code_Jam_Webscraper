//	GCJ 2010 Round 2 (A)

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

int K;
int M;
int A[210][210];
int a[210][210];

int main() {
	int i, x, y;
	int dx, dy;
	
	for (int TC = in(), tc = 0; ++tc <= TC; ) {
		K = in();
		for (i = 0; i < K; ++i) {
			for (x = i, y = 0; x >= 0; --x, ++y) {
				A[x][y] = in();
			}
		}
		for (i = 1; i < K; ++i) {
			for (x = K - 1, y = i; y < K; --x, ++y) {
				A[x][y] = in();
			}
		}
//for(x=0;x<K;++x)pv(A[x],A[x]+K);
		for (M = K; ; ++M) {
			for (dx = 0; dx <= M - K; ++dx) for (dy = 0; dy <= M - K; ++dy) {
				if (dx != 0 && dx != M - K && dy != 0 && dy != M - K) continue;
				memset(a, ~0, sizeof(a));
				for (x = 0; x < K; ++x) for (y = 0; y < K; ++y) {
					a[x + dx][y + dy] = A[x][y];
				}
				for (x = 0; x < M; ++x) for (y = 0; y < M; ++y) {
					if (~a[x][y] && ~a[y][x] && a[x][y] != a[y][x]) {
						goto failed;
					}
					if (~a[x][y] && ~a[M - 1 - y][M - 1 - x] && a[x][y] != a[M - 1 - y][M - 1 - x]) {
						goto failed;
					}
				}
				goto found;
			failed:;
			}
		}
	found:;
		printf("Case #%d: %d\n", tc, M * M - K * K);
	}
	
	return 0;
}

