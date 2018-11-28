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
#define left huyleft
#define right huyright
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "A"
#define RR 151

int a[256];

void solve () {
	int n;
	scanf("%d", &n);
	int S = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &a[i]);
		S += a[i];
	}
	for (int i = 0; i < n; ++i) {
		double l = 0.0, r = 1.0;
		for (int it = 0; it < 256; ++it) {
			double m = (l + r) / 2.0;
			double cur = a[i] + S * m;
			double sum = m;
			for (int j = 0; j < n; ++j) {
				if (a[j] >= cur || i == j) continue;
				sum += (cur - a[j]) / S;
			}
			if (sum > 1.0)
				r = m;
			else
				l = m;
		}
		double res = (l + r) / 2.0;
		printf("%.15lf ", res * 100.0);
	}
	puts("");
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt1.in", "r", stdin);
    freopen(TASK "-small-attempt1.out", "w", stdout);
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
