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

struct walkway {
	int b,e,w;
	int R, S;
	double t;

	bool operator<(const walkway& x) const {
		double f = (double)(e-b)/(w+S) - (double)(e-b)/(w+R);
		double s = (double)(x.e-x.b)/(x.w+x.S) - (double)(x.e-x.b)/(x.w+x.R);

		return f/(e-b) < s/(x.e-x.b);
	}

};

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T;	cin >> T;
	for(int tc = 1; tc <= T; ++tc) {

		int X,S,R,t,N;
		cin >> X >> S >> R >> t >> N;

		vector<walkway> vw(N+1);
		int sm = 0;
		for(int i = 0; i < N; ++i) {
			cin >> vw[i].b >> vw[i].e >> vw[i].w;
			vw[i].S = S;
			vw[i].R = R;
			sm += vw[i].e - vw[i].b;
		}
		vw[N].b = 0; vw[N].e = X - sm;
		vw[N].w = 0;
		vw[N].S = S;
		vw[N].R = R;

		sort(vw.rbegin(), vw.rend());
		double dt = (double)t;
		double ans = 0;

		for(int i = 0; i < N+1; ++i) {
			double xt = 0.0;
			if( dt > 0 ) {
				xt = (double)(vw[i].e - vw[i].b)/(vw[i].w + R);
				if( xt > dt ) {
					xt = dt + (vw[i].e - vw[i].b - (vw[i].w + R)*dt) / (vw[i].w + S);
					dt = 0;
				} else {
					dt -= xt;
				}
			} else {
				xt = (double)(vw[i].e - vw[i].b)/(vw[i].w + S);
			}
			vw[i].t = xt;
			ans += vw[i].t;
		}


		cout << "Case #" << tc << ": " << fixed << setprecision(10) << ans << endl;
	}


	return 0;
}
