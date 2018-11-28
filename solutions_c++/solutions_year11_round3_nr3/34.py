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

int64 gcd (int64 a, int64 b) {
	return b ? gcd(b, a % b) : a;
}

int n;
int64 L, H;
int64 a[1 << 14];
int64 l[1 << 14];
int64 g[1 << 14];

inline int64 lcm (int64 a, int64 b) {
	int64 g = gcd(a, b);
	a /= g;
	if (b <= H / a) return a * b;
	return H + 10;
}

void solve () {
	cin >> n >> L >> H;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	a[n++] = 1;
	sort(a, a + n);
	n = unique(a, a + n) - a;
	
	int64 res = H + 10;
	for (int i = 0; i < n; ++i)
	{
		int64 l = 1, g = 0;
		for (int j = 0; j <= i; ++j)
			l = lcm(l, a[j]);
		for (int j = i + 1; j < n; ++j)
			g = gcd(g, a[j]);
		
		if (l > H) break;
		if (g % l) continue;

		if (g == 0)
		{
			int64 x = l;
			if (x < L) x *= (L / l);
			if (x < L) x += l;
			if (x <= H) res = min(res, x);
			continue;
		}

		int64 x = l;
		for (int64 j = 1; j * j <= g; ++j)
		{
			if (g % j) continue;
			int64 t = j;
			if (t % l == 0 && t <= H && t >= L) res = min(res, t);
			t = g / j;
			if (t % l) continue;
			if (t <= H && t >= L) res = min(res, t);
		}
	}

	if (res > H)
		puts("NO");
	else
		printf("%lld\n", res);
}

int main() { 
    //freopen("input.txt", "r", stdin);  freopen("output.txt", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin);  freopen("B-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);  freopen("C-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cerr << test << endl;
		printf("Case #%d: ", test);
		solve();
	}

    return 0; 
}