#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

const double eps = 10e-8;

int solution(int nTest) {
	int x;
	int s;
	int R;
	int t;
	int n;
	scanf("%d%d%d", &x, &s, &R);
	scanf("%d%d", &t, &n);
	vector<pair<pii, int> > walk;

	For(i, 0, n) {
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);
		walk.pb(mp(mp(b, e), w));
	}
	walk.pb(mp(mp(0, 0), 0));
	walk.pb(mp(mp(x, x), 0));
	sort(all(walk));

	double res = 0.;

	vector<pair<pair<double, double>, pair<double, double> > > dist;


	double m = R - s;


	For(i, 1, sz(walk)) {
		double x = walk[i].first.first - walk[i-1].first.second;
		double a = s;
		dist.pb(mp(mp(x/a, 0), mp(x, a)));
		x = walk[i].first.second - walk[i].first.first;
		a = (double)walk[i].second + s;
		
		dist.pb(mp(mp(-(double)(a + m)/m, 0), mp(x, a)));
	}

	sort(all(dist));
	double a = t;

	reverse(all(dist));

	For(i, 0, sz(dist)) {
		double x = dist[i].second.first;
		double s = dist[i].second.second;

		if(a <= 0.) {
			res += dist[i].second.first / dist[i].second.second;
		}
		else {
			double vr = x / (s + m);
			if(vr < a) {
				a -= vr;
				res += vr;
			}
			else {
				res += a;
				res += (x - (s + m) * a) / s;
				a = 0.;
			}
		}

	}
	printf("Case #%d: ", nTest + 1);

	printf("%.7lf\n", res);

	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;

	scanf("%d", &n);

	while(i < n && solution(i))
		i++;

	return 0;
}

