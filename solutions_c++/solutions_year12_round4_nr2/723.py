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
#define TASK "B"
#define RR 151

struct vect {
	double x, y;
	vect (double x = 0, double y = 0)
		: x (x), y (y) {}
	vect rotate (double angle) const {
		double cs = cos(angle), sn = sin(angle);
		double nx = x * cs - y * sn;
		double ny = x * sn + y * cs;
		return vect(nx, ny);
	}
	vect norm (double len = 1) const {
		double m = md();
		return vect(x * len / m, y * len / m);
	}
	double md () const {
		return sqrt(x * x + y * y);
	}
	vect operator + (const vect &o) const {
		return vect(x + o.x, y + o.y);
	}
	vect operator - (const vect &o) const {
		return vect(x - o.x, y - o.y);
	}
};

int n, W, L;
int r[1 << 10];
pii a[1 << 10];
int pos[1 << 10];
vector<vect> ans;

inline double p2p (vect a, vect b) {
	return (a - b).md();
}

inline double my_acos (double angle) {
	angle = min(angle, 1.0);
	angle = max(angle, -1.0);
	return acos(angle);
}

inline bool check (vect p, double R) {
	bool res = true;
	res &= 0.0 <= p.x && p.x <= W;
	res &= 0.0 <= p.y && p.y <= L;
	for (int i = 0; i < sz(ans) && res; ++i)
		res &= (ans[i] - p).md() + eps >= r[i] + R;
	return res;
}

bool place (int x) {
	if (sz(ans) == n) return true;
	double R = r[x];
	for (int i = 0; i < sz(ans); ++i) {
		for (int j = 0; j < sz(ans); ++j) {
			if (i == j) continue;
			double d = p2p(ans[i], ans[j]);
			if (d - r[i] - r[j] - eps > 2 * R) continue;
			double cs = (sqr(R + r[i]) + sqr(d) - sqr(R + r[j])) / (2.0 * (R + r[i]) * d);
			double angle = my_acos(cs);
			vect cur;
			cur = ans[i] + (ans[j] - ans[i]).rotate(angle).norm(r[i] + R);
			if (check(cur, R)) {
				ans.push_back(cur);
				if (place(x + 1)) return true;
				ans.pop_back();
			}
			cur = ans[i] + (ans[j] - ans[i]).rotate(-angle).norm(r[i] + R);
			if (check(cur, R)) {
				ans.push_back(cur);
				if (place(x + 1)) return true;
				ans.pop_back();
			}
		}
	}
	return false;
}

void ass (bool b) {
	if (!b) cerr << "fail\n";
}

void solve () {
	scanf("%d%d%d", &n, &W, &L);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &r[i]);
		a[i] = MP(r[i], i);
	}
	sort(a, a + n);
	//reverse(a, a + n);
	for (int i = 0; i < n; ++i)
		r[i] = a[i].first, pos[a[i].second] = i;
	ans.clear();
	int i = 0;
	if (W >= L) {
		int x = 0;
		for (; i < n; ++i) {
			if (i) x += r[i];
			if (x > W) break;
			ans.push_back(vect(x + 0.0, 0.0));
			x += r[i];
		}
	} else {
		int y = 0;
		for (; i < n; ++i) {
			if (i) y += r[i];
			if (y > L) break;
			ans.push_back(vect(0.0, y + 0.0));
			y += r[i];
		}
	}
	place(i);
	ass(sz(ans) == n);
	for (int i = 0; i < sz(ans); ++i)
		for (int j = i + 1; j < sz(ans); ++j)
			ass((ans[i] - ans[j]).md() + eps >= r[i] + r[j]);
	for (int i = 0; i < sz(ans); ++i)
		printf("%.15lf %.15lf ", ans[pos[i]].x, ans[pos[i]].y);
	puts("");
}

//#define DEBUG
#define SMALL
//#define LARGE

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
