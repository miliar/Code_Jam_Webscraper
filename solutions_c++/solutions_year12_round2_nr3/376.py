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
#define TASK "C"
#define RR 151

int a[32];
vector<int> *sums;

void solve () {
	int n;
	cin >> n;
	sums = new vector<int>[1 << 21];
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int mask = 1; mask < (1 << n); ++mask) {
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			if (mask & (1 << i))
				sum += a[i];
		}
		sums[sum].push_back(mask);
	}
	for (int sum = 1; sum < (1 << 21); ++sum) {
		if (sums[sum].empty()) continue;
		for (int i = 0; i < sz(sums[sum]); ++i) {
			for (int j = i + 1; j < sz(sums[sum]); ++j) {
				if ((sums[sum][i] & sums[sum][j]) == 0) {
					puts("");
					for (int k = 0; k < n; ++k)
						if (sums[sum][i] & (1 << k))
							printf("%d ", a[k]);
					puts("");
					for (int k = 0; k < n; ++k)
						if (sums[sum][j] & (1 << k))
							printf("%d ", a[k]);
					puts("");
					return;
				}
			}
		}
	}
	puts("Impossible");
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
    freopen(TASK "-large-practice.in", "r", stdin);
    freopen(TASK "-large-practice.out", "w", stdout);
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
