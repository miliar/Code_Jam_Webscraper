//	GCJ 2010 Round 3 (A)

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

Int TEN[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, };

const int LIM = 1100005;
int isnp[1100010];
int len, ps[1100010];

void prpr() {
	int i, j;
	for (i = 2; i * i < LIM; ++i) if (!isnp[i]) {
		for (j = i * i; j < LIM; j += i) isnp[j] = 1;
	}
	for (i = 2; i < LIM; ++i) if (!isnp[i]) {
		ps[len++] = i;
	}
}

Int mod(Int a, Int m) { return (a % m + m) % m; }

Int gojo(Int a, Int b, Int &x, Int &y) {	//	ax + by == gcd(a, b)
	if (b) { Int g = gojo(b, a % b, y, x); y -= (a / b) * x; return g; }
	x = 1; y = 0; return a;
}

Int gcd(Int a, Int b) { return b ? gcd(b, a % b) : a; }
Int lcm(Int a, Int b) { return a / gcd(a, b) * b; }

Int modInv(Int a, Int m) {	//	ax == 1 (m)
	Int x, y; gojo(a, m, x, y);
	return mod(x, m);
}


int D, K;
Int S[20];

int main() {
	int i, j;
	Int dai;
	
	prpr();
	
	for (int TC = in(), tc = 0; ++tc <= TC; ) {
		D = in();
		K = in();
		for (i = 0; i < K; ++i) {
			S[i] = in();
		}
		dai = *max_element(S, S + K);
		Int ans = -1, tmp;
		Int p, a, b;
		if (K == 1) goto failed;
		if (S[0] == S[1]) {
			ans = S[0];
			goto done;
		}
		if (K == 2) goto failed;
		for (j = 0; j < len; ++j) {
			p = ps[j];
			if (p <= dai) continue;
			if (p > TEN[D]) break;
			a = mod(S[2] - S[1], p) * modInv(mod(S[1] - S[0], p), p) % p;
			b = mod(S[1] - a * S[0], p);
//cout<<p<<" "<<a<<" "<<b<<endl;
			for (i = 1; i < K; ++i) {
				if (S[i] != mod(a * S[i - 1] + b, p)) break;
			}
			if (i == K) {
				tmp = mod(a * S[K - 1] + b, p);
				if (ans < 0) ans = tmp;
				if (ans != tmp) goto failed;
			}
		}
	done:;
		printf("Case #%d: %lld\n", tc, ans);
		continue;
	failed:;
		printf("Case #%d: I don't know.\n", tc);
	}
	
	return 0;
}

