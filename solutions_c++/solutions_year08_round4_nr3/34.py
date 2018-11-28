#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))


using namespace std;

#define maxn 1005

int n;
int x[maxn], y[maxn], z[maxn], p[maxn];

struct par {
	double a[4], b[4];
};

bool isect(par u, par v, par &w) {
	par c;
	FOR(i, 4) {
		if (u.b[i] < v.a[i] || u.a[i] > v.b[i]) return false;
		c.a[i] = max(u.a[i], v.a[i]);
		c.b[i] = min(u.b[i], v.b[i]);
	}
	w = c;
	return true;
}

par make(double x, double y, double z, double d) {
	par res;
	double t[4];
	t[0] = x + y + z;
	t[1] = x + y - z;
	t[2] = x - y + z;
	t[3] = x - y - z;
	FOR(i, 4) {
		res.a[i] = t[i] - d;
		res.b[i] = t[i] + d;
	}
	return res;
}

void solvecase() {
	scanf("%d", &n);
	FOR(i, n) {
		scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);
	}
	double l = 0, r = 1e8;
	FOR(it, 100) {
		double m = (l + r) / 2;
		bool ok = true;
		par cur = make(x[0], y[0], z[0], m * p[0]);
		for (int i = 1; i < n; i++) {
			if (!isect(cur, make(x[i], y[i], z[i], m * p[i]), cur)) {
				ok = false;
				break;
			}
		}
		if (ok) r = m; else l = m;
	}
	printf("%.7lf", r);	
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}