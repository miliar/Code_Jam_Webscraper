#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 1005;

int n, m;
double X, S, R, t;
double b[MAXN];
double e[MAXN];
double w[MAXN];
int h[MAXN];
const double eps = 1e-9; 
double x, ans;

void move(double d, double sp) {
	if (d < eps) {
		return;
	}
	double ct = d / sp;
	if (ct > t - eps) {
		ans += t;
		d -= sp * t;
		t = INF;
		sp -= R - S;
		R = S;
		ct = d / sp;
	}
	ans += ct;
	t -= ct;
}

bool cmp(int id1, int id2)
{
	return w[id1] < w[id2];
}

void solve() {
	int i, j, k;
	scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &n);
	for (i = 0; i < n; ++ i)
	{
		scanf("%lf %lf %lf", &b[i], &e[i], &w[i]);
	}
	x = 0;
	ans = 0;
	double dist = 0;
	for (i = 0; i < n; ++ i) {
		dist += b[i] - x;
		x = e[i];
		h[i] = i;
	}
	dist += X - x;
	move(dist, R);
	sort(h, h + n, cmp);
	for (i = 0; i < n; ++ i) {
		double sp = R;
		double dd = e[h[i]] - b[h[i]];
		sp = R + w[h[i]];
		move(dd, sp);
	}
	printf("%.12lf\n", ans);
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}