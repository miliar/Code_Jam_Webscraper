#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 1000;

int T, n, cas = 1;
struct plant {
	double x, y, r;
}p[50];

double dist(plant a, plant b) {
	double xx = a.x - b.x;
	double yy = a.y - b.y;
	return sqrt(xx * xx + yy * yy);
}

void solve() {
	printf("Case #%d: ", cas++);
	if(n == 1) {
		printf("%.6lf\n", p[0].r);
		return;
	}
	if(n == 2) {
		printf("%.6lf\n", max(p[0].r, p[1].r));
		return;
	}
	double ans = inf;
	double tmp;
	tmp = max(p[0].r, (dist(p[1], p[2]) + p[1].r + p[2].r) / 2);
	ans = min(tmp, ans);

	tmp = max(p[1].r, (dist(p[2], p[0]) + p[2].r + p[0].r) / 2);
	ans = min(tmp, ans);

	tmp = max(p[2].r, (dist(p[1], p[0]) + p[1].r + p[0].r) / 2);
	ans = min(tmp, ans);

	printf("%.06lf\n", ans);
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	cin >> T;
	while(T--) {
		cin >> n;
		for(int i = 0; i < n; i++) {
			scanf("%lf %lf %lf", &p[i].x, &p[i].y, &p[i].r);
		}
		solve();
	}

	return 0;
}

/*Powered By Lynn-Beta1*/