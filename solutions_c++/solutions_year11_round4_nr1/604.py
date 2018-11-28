#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

void main() {
	int T, X, S, R, TMP, N;
	int b, e, w;
	vector<pair<int, int> > ways;
	deque<pair<int, int> > spd;

	cin >> T;

	int i,j;
	REP(i,T) {
		ways.clear();
		spd.clear();
		cin >> X >> S >> R >> TMP >> N;
		double t = TMP;
		REP(j, N) {
			cin >> b >> e >> w;
			ways.pb(make_pair(b, w));
			ways.pb(make_pair(e, -w));
		}

		sort(all(ways));

		int len = ways[0].first;
		int sp = 0;

		spd.pb(make_pair(sp,len));

		int n = ways.size();

		FOR(j,1,n-1) {
			if (ways[j-1].first == ways[j].first)
				continue;

			len = ways[j].first - ways[j-1].first;
			if (ways[j-1].second < 0) {
				sp = 0;
			} else {
				sp = ways[j-1].second;
			}
			spd.pb(make_pair(sp,len));
		}

		len = X - ways[n-1].first;
		sp = 0;
		if (len > 0)
			spd.pb(make_pair(sp,len));

		sort(all(spd));

		n = spd.size();
		double res = 0;
		REP(j,n) {
			if (t <= 0.0000000001)
				res += spd[j].second / ((double)spd[j].first + S);
			else {
				double nsp = spd[j].first + R;
				double est = spd[j].second / nsp;
				if (t >= est) {
					res += est;
					t -= est;
				} else {
					double nlen = t * nsp;
					double rlen = spd[j].second - nlen;
					res += t + rlen / ((double)spd[j].first + S);
					t = 0;
				}
			}
		}

		cout << "Case #" << i+1 << ": ";
		printf("%.9lf\n", res);
	}
}