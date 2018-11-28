#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
//#include <ctime>
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
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "B"
#define RR 151

int n;
pii a[1 << 11];
map<pii, int> d;

int rec (int mask, int sum) {
	if ((mask ^ (mask >> 1)) == (1 << (n << 1)) - 1)
		return 0;
	if (d.count(MP(mask, sum)))
		return d[MP(mask, sum)];
	int &res = d[MP(mask, sum)];
	res = inf;
	for (int i = 0; i < n; ++i) {
		int val = (mask >> (i << 1)) & 3;
		if (val == 0) {
			if (a[i].first <= sum)
				res = min(res, rec(mask | (1 << (i << 1)), sum + 1) + 1);
			if (a[i].second <= sum)
				res = min(res, rec(mask | (2 << (i << 1)), sum + 2) + 1);
		}
		if (val == 1) {
			if (a[i].second <= sum)
				res = min(res, rec(mask ^ (3 << (i << 1)), sum + 1) + 1);
		}
	}
	return res;
}

//int d[1 << 11][2];
//
//int rec (int sum, int inc) {
//	int &res = d[sum][inc];
//	if (res != -1) return res;
//	bool done = true;
//	for (int i = 0; i < n; ++i)
//		done &= a[i].second < sum;
//	if (done)
//		return res = 0;
//	res = inf;
//	for (int i = 0; i < n; ++i) {
//		for (int j = 0; j <= inc; ++j) {
//			if (a[i].first == sum - j || a[i].first != a[i].second && a[i].second == sum - j)
//				res = min(res, rec(sum + 1, 0) + 1);
//		}
//	}
//	for (int i = 0; i < n; ++i) {
//	}
//}

void solve () {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d%d", &a[i].first, &a[i].second);
	//memset(d, -1, sizeof d);
	d.clear();
	int res = rec(0, 0);
	if (res == inf)
		puts("Too Bad");
	else
		printf("%d\n", res);
}

//#define DEBUG
#define SMALL
//#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);

        printf("Case #%d: ", test);

        solve();
        
        fprintf(stderr, "done.\n");
    }
    return 0;
}
