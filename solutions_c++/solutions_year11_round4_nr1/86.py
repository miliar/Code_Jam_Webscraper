#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define REP(i, end) for(int i = 0; i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

int main() {
    int cases;
    cin >> cases;
    cout.precision(12);
    for (int cs = 1; cs <= cases; cs++) {
	double x, s, r, t;
	int n;
	cin >> x >> s >> r >> t >> n;

	vector<pair<double, double> > v;
	REP(i, n) {
	    double b, e, w;
	    cin >> b >> e >> w;
	    v.push_back(make_pair(w, e-b));
	    x -= e-b;
	}
	v.push_back(make_pair(0, x));

	sort(v.begin(), v.end());

	double res = 0;
	FOREACH(p, v) {
	    if (t > 0) {
		double a = p->second/(p->first+r);
		if (a <= t) {
		    res += a;
		    t -= a;
		}
		else {
		    res += t+(p->second-(p->first+r)*t)/(p->first+s);
		    t = 0;
		}
	    }
	    else
		res += p->second/(p->first+s);
	}
	cout << "Case #" << cs << ": " << res << endl;
    }
}
