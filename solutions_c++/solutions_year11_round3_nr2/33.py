#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
 
#include <algorithm> 
#include <bitset> 
#include <cassert> 
#include <climits> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 
 
using namespace std; 
 
#pragma comment(linker, "/STACK:64000000") 
 
template<class T> inline T sqr (T x) {return x * x;} 
 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> pip; 
typedef pair<pii, int> ppi; 
typedef pair<int64, int64> pii64; 
typedef pair<double, double> pdd; 
typedef pair<string, int> psi; 
typedef pair<int, string> pis; 
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
#define FAIL ++*(int*)0 
#define eps  1e-9 
#define inf  0x7f7f7f7f 
#define MP make_pair 
#define sz(C) (int)((C).size()) 
#define all(C) (C).begin(), (C).end() 
#define TASK "test" 
#define RR 151 

int L, n, C;
int64 t;
int64 a[1 << 17];
int b[1 << 17];

inline int64 move () {
	int64 res = 0;
	for (int i = 0; i < n; ++i) {
		if (!b[i])
			res += a[i];
		else {
			if (res >= t) {
				res += a[i] >> 1;
				continue;
			}
			if (res + a[i] <= t) {
				res += a[i];
				continue;
			}
			int64 dt = t - res;
			res += dt;
			res += (a[i] - dt) / 2;
		}
	}
	return res;
}

void solve () {
	cin >> L >> t >> n >> C;
	for (int i = 0; i < C; ++i) {
		cin >> a[i];
		a[i] <<= 1;
	}
	for (int i = C; i < n; ++i)
		a[i] = a[i % C];
	int64 res = accumulate(a, a + n, 0ll);
	memset(b, 0, sizeof b);
	if (L)
	for (int i = 0; i < n; ++i) {
		b[i] = true;
		res = min(res, move());
		b[i] = false;
	}
	if (L > 1)
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			b[i] = b[j] = true;
			res = min(res, move());
			b[i] = b[j] = false;
		}
	}
	printf("%lld\n", res);
}

int main() { 
    //freopen("input.txt", "r", stdin);  freopen("output.txt", "w", stdout);
	freopen("B-small-attempt0.in", "r", stdin);  freopen("B-small-attempt0.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);  freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		solve();
	}

    return 0; 
}