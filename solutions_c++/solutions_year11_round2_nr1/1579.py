#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> II;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define REP(i,n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<b; i++)

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout );

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout );

	int tt;
	cin >> tt;
	cerr << "T=" << tt << endl;

	for (int t = 1; t <= tt; ++t) {
		int cnt;
		cin >> cnt;
		cerr << "CNT:" << cnt << endl;

		vector<string> m;
		REP(i,cnt) {
			string s;
			cin >> s;
			m.push_back(s);
			// cerr << s << endl;
		}
		TR(m, it) {
			cerr << *it << endl;
		}

		vector<double> wp;

		REP(i, sz(m)) {
			int total = 0;
			int won = 0;
			REP(k, sz(m)) {
				if (m[i][k] != '.')
					total++;
				if (m[i][k] == '1')
					won++;
			}
			wp.push_back((double) won / total);
			cerr << "CMD " << i << ": total=" << total << " won=" << won
					<< " wp=" << wp[i] << endl;
		}

		vector<double> owp;
		REP(d, sz(m)) {
			double wps = 0;
			int cs = 0;
			// calc wp
			REP(i, sz(m)) {
				if (m[d][i] == '.')
					continue;

				int total = 0;
				int won = 0;
				REP(k, sz(m)) {
					if (k == d)
						continue;
					if (m[i][k] != '.')
						total++;
					if (m[i][k] == '1')
						won++;
				}
				double w = (double) won / total;
				cerr << "wps for " << d << " cmd=" << i << " w=" << w << endl;
				wps += w;
				cs++;
			}
			owp.push_back(wps / cs);
			cerr << "CMD " << d << ": owp=" << owp[d] << endl;
		}

		vector<double> oowp;
		REP(d, sz(m)) {
			double wps = 0;
			int cs = 0;
			// calc wp
			REP(i, sz(m)) {
				if (m[d][i] == '.') continue;
				wps += owp[i];
				cs++;
				cerr << "oowp for " << d << " cmd=" << i << " owp=" << owp[i] << endl;
			}
			oowp.push_back(wps / cs);
			cerr << "CMD " << d << ": oowp=" << oowp[d] << endl;
		}

		printf("Case #%d:\n", t );
		REP(i, cnt) {
			 double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			 cerr << "rpi " << i << rpi << endl;
			 printf("%.12f\n", rpi);
		}
	}

	return 0;
}
