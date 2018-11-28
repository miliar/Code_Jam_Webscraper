#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <limits>
#include <complex>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef vector<int> vint;
typedef set<int> sint;
typedef long double ld;

#define rep(i, a, b) for(int i=(a); i<(b); ++i)
#define clr(a, v) memset((a), (v), sizeof(a))
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()

int const inf = 0x7f7f7f7f;
ll const llinf = 0x7f7f7f7f7f7f7f7fll;
ld const eps = 1e-9;

void frr(){	freopen("test.in", "r", stdin); }

template<typename T> inline bool setmin(T &a, T const &b) { if(b < a) { a = b; return true; } else return false; }
template<typename T> inline bool setmax(T &a, T const &b) { if(a < b) { a = b; return true; } else return false; }

template<typename A, typename B> inline A& _0(pair<A, B> &p) { return p.first; }
template<typename A, typename B> inline B& _1(pair<A, B> &p) { return p.second; }
template<typename A> inline A _0(complex<A> &z) { return z.real(); }
template<typename A> inline A _1(complex<A> &z) { return z.imag(); }
template<typename A> inline A& _0(A *p) { return p[0]; }
template<typename A> inline A& _1(A *p) { return p[1]; }

// dp[mask] - the maximal sum, which can be acheived with mask m.

int const max_n = 1024;
int const max_s = 1<<20;
int a[max_n], dp[2][max_s];

int test_case = 0;

void solve_case()
{
	++ test_case;

	int n; cin >> n;
	rep (i, 0, n) { 
		cin >> a[i]; 
	}

	int prev = 0, next = 1;
	clr(dp[prev], -1);
	dp[prev][0] = 0;

	rep (i, 0, n) {
		clr(dp[next], -1);
		rep (mask, 0, max_s) {
			if (dp[prev][mask] != -1) {
				if (dp[next][mask] == -1 || dp[next][mask] < dp[prev][mask])
					dp[next][mask] = dp[prev][mask];
				if (dp[next][mask ^ a[i]] == -1 || dp[next][mask ^ a[i]] < a[i] + dp[prev][mask])
					dp[next][mask ^ a[i]] = a[i] + dp[prev][mask];
			}
		}

		swap(prev, next);
	}

	int s_mask = 0;
	rep (i, 0, n) s_mask ^= a[i];

	int res = -1;
	rep (mask, 1, max_s) {
		if ( dp[prev][mask] != -1 && mask == (s_mask ^ mask) ) {
			if (res == -1 || res < dp[prev][mask])
				res = dp[prev][mask];
		}
	}

	printf("Case #%d: ", test_case);

	if (res == -1) {
		printf("NO\n");
	}
	else {
		printf("%d\n", res);
	}
}

int main()
{
	//frr();
	int t; cin >> t;
	while(t--) solve_case();
	return 0;
}
