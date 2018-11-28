#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T a) {return a > 0 ? a : (-a); }
template<class T> T sqr(T a) {return a * a; }

using namespace std;

bool www = false;

double getS(const vector<pair<int, int> > &a, double x) {
	int n = sz(a);
	double ans = 0;
//	if (www) printf("x=%.10lf, n=%d\n", x, n);
	for (int i = 0; i < n - 1; ++i)
		if (i == n - 2 || a[i + 1].first > x) {
			double y = a[i].second + (a[i + 1].second - a[i].second + 0.0) * (x - a[i].first + 0.0) / (a[i + 1].first - a[i].first + 0.0);
//			if (www) printf("y=%.10lf\n", y);
			ans += (a[i].second + y + 0.0) * (x - a[i].first) / 2.0;
			break;
		}
		else {
			ans += (a[i].second + a[i + 1].second + 0.0) * (a[i + 1].first - a[i].first + 0.0) / 2.0;
		}
	return ans;
}

double getS(const vector<pair<int, int> > &a, const vector<pair<int, int> > &b, double x) {
	return getS(b, x) - getS(a, x);
}

void solve(int testnum) {
	cerr << testnum << endl;
	int w, l, u, g;
	scanf("%d%d%d%d", &w, &l, &u, &g);
	vector<pair<int, int> > L(l), U(u);
	for (int i = 0; i < l; ++i) scanf("%d%d", &L[i].first, &L[i].second);
	for (int i = 0; i < u; ++i) scanf("%d%d", &U[i].first, &U[i].second);
	double S = getS(L, U, w);
	printf("Case #%d:\n", testnum);
	for (int i = 1; i < g; ++i) {
		double need = S * i / g;
		double LL = 0;
		double RR = w;
		for (int it = 0; it < 500; ++it) {
			double tmp = (LL + RR) / 2;
			if (getS(L, U, tmp) > need)
				RR = tmp; else LL = tmp;
		}
		www = true;
//		printf("%.10lf %.10lf\n", need, getS(L, U, (LL + RR) / 2));
		www = false;
		printf("%.10lf\n", (LL + RR) / 2);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) solve(i);
}
