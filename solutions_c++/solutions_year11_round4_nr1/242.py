#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int X, S, R, N;
double t;
int beg[10100], end[10100], w[10100];

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> X >> S >> R >> t >> N;
		REP(i, N) cin >> beg[i] >> end[i] >> w[i];
		vector<pair<double, double> > info;
		double totaltime = 0.0;
		int totaldist = 0;
		REP(i, N) {
			info.pb(make_pair(double(R-S)/(S+w[i]), double(end[i]-beg[i])/(R+w[i])));
			totaltime += double(end[i]-beg[i])/(S+w[i]);
			totaldist += end[i] - beg[i];
		}
		if (totaldist < X) {
			info.pb(make_pair(double(R-S)/(S), double(X-totaldist)/(R)));
			totaltime += double(X-totaldist)/(S);
		}
		sort(all(info));
		reverse(all(info));
		//cout << totaltime << endl;
		REP(i, SZ(info)) {
			if (t <= 0.0) break;
			double cuant = min(t,info[i].second);
			totaltime -= cuant * info[i].first;
			t -= cuant;
		}
		cout << "Case #" << caso+1 << ": " << fixed << setprecision(6) << totaltime << endl;
	}
	return 0;
}
