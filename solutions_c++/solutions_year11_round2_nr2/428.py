#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

#define V second

typedef long long llong;
typedef long double ldouble;
typedef pair<ldouble, ldouble> pli;

vector<pli> points;
llong n, D;

bool cando(ldouble time){
	ldouble left = points[0].first - time;

	for (int i = 0; i < n; ++i){
		if (points[i].first + time < left){
			return false;
		}
 		left = max(left, points[i].first - time);
 		if (left + D * (points[i].V - 1) > points[i].first + time ){
 			return false;
 		}
 		else {
 			left += D * points[i].V;
 		}
	}
	return true;
}

ldouble solve(){
	cin >> n >> D;
	points.resize(n);
	for (int i = 0; i < n; ++i)
		cin >> points[i].first >> points[i].V;

	ldouble l = 0, r = 1e+12 + 100000, m;
	const ldouble eps = 1e-9;
	long cnt = 0;
	while (r - l > eps){
		++cnt;
		m = (l + r) / 2;
		if (cnt > 100000)
			return l;
		if (cando(m))
			r = m;
		else
			l = m;

	}
	return l;
}

int main()
{
#if 1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	cout.precision(10);
	for (int test = 1; test <= T; ++test){
		double time = solve();
		printf("Case #%d: %.8lf\n", test, time);
	}

	return 0;
}
