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
#define TASK "A"
#define RR 151

int n, m;
double p[1 << 17];
double prod[1 << 17];

double keep_typing () {
	double cur = 1.0;
	for (int i = 0; i < n; ++i)
		cur *= p[i];
	return cur * (m - n + 1) + (1.0 - cur) * (m - n + 1 + m + 1);
}

double press_enter () {
	return 1 + m + 1;
}

inline double get_prob (int l, int r) {
	if (l > r) return 0.0;
	return prod[r] / (l ? prod[l - 1] : 1.0);
}

void solve () {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &p[i]);
	for (int i = 0; i < n; ++i) {
		prod[i] = p[i];
		if (i) prod[i] *= prod[i - 1];
	}

	vector<double> res (1 + n + 1, 0.0);
	res[0] = keep_typing();
	for (int cnt = 1; cnt <= n; ++cnt) {
		double all_correct = get_prob(0, n - cnt - 1);
		res[cnt] = all_correct * (cnt + (m - (n - cnt)) + 1) + (1.0 - all_correct) * (cnt + (m - (n - cnt)) + 1 + m + 1);
	}
	res[sz(res) - 1] = press_enter();
	printf("%.15lf\n", *min_element(all(res)));

}

//#define DEBUG
//#define SMALL
#define LARGE

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
