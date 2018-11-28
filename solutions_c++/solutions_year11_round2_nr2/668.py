/**
 *
 */
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

bool feasible( vi& p, int D, double t ) {
	double prev = (double)p[0] - 2*t - 2*D - 100.0;

	for(int i = 0; i < sz(p); ++i) {
		double cur = prev + D;

		if( p[i] >= cur ) {
			cur = max(cur, p[i] - t);
		} else {
			if( p[i] + t < cur-1e-9 && !(p[i] + t < cur) )
				cerr << "precision problem" << endl;

			if( p[i] + t < cur )
				return false;
			cur = min(cur, p[i] + t);
		}

		prev = cur;
	}

	return true;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T; cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		int C, D; cin >> C >> D;

		vii pv(C);
		for(int i = 0; i < C; ++i)
			cin >> pv[i].first >> pv[i].second;

		vi pos;
		for(int i = 0; i < sz(pv); ++i)
			for(int j = 0; j < pv[i].second; ++j)
				pos.push_back(pv[i].first);


		double ans = 0.0;

		if( feasible(pos, D, 0.0) )
			ans = 0.0;
		else {
			double lo = 0.0;
			double hi = 1e8;
			while( !feasible(pos,D,hi) )
				hi *= 2.0;

			while( hi-lo > 1e-10 ) {
				double mid = 0.5*(lo+hi);
				if( feasible(pos, D, mid) )
					hi = mid;
				else
					lo = mid;
			}
			ans = hi;
		}

		cout << "Case #" << tc << ": " << fixed << setprecision(10) << ans << "\n";
	}


	return 0;
}
