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
    for (int cs = 1; cs <= cases; cs++) {
	cout << "Case #" << cs << ":" << endl;

	int w, l, u, g;
	cin >> w >> l >> u >> g;

	set<int> xs;
	vector<pair<int, int> > lp, up;

	REP(i, l) {
	    int x, y;
	    cin >> x >> y;
	    xs.insert(x);
	    lp.push_back(make_pair(x, y));
	}

	REP(i, u) {
	    int x, y;
	    cin >> x >> y;
	    xs.insert(x);
	    up.push_back(make_pair(x, y));
	}

	int n = xs.size();
	vector<double> x, y1(n), y2(n), y(n);

	FOREACH(i, xs)
	    x.push_back(*i);


	REP(i, l)
	    REP(j, n)
		if (x[j] == lp[i].first)
		    y1[j] = lp[i].second;

	for (int i = 1; i < l; i++) {
	    int j = 0;
	    while (x[j] != lp[i-1].first)
		j++;
	    int k = j;
	    while (x[k] != lp[i].first)
		k++;
	    for (int p = j+1; p < k; p++)
		y1[p] = y1[j] + (x[p]-x[j])*(y1[k]-y1[j])/(x[k]-x[j]);
	}


	REP(i, u)
	    REP(j, n)
		if (x[j] == up[i].first)
		    y2[j] = up[i].second;

	for (int i = 1; i < u; i++) {
	    int j = 0;
	    while (x[j] != up[i-1].first)
		j++;
	    int k = j;
	    while (x[k] != up[i].first)
		k++;
	    for (int p = j+1; p < k; p++)
		y2[p] = y2[j] + (x[p]-x[j])*(y2[k]-y2[j])/(x[k]-x[j]);
	}


	REP(i, n)
	    y[i] = y2[i]-y1[i];

	/*
	for (int i = 0; i < n; i++)
	    cout << x[i] << " " << y1[i] << " " << y2[i] << " " << y[i] << endl;
	    */

	vector<double> s(n);
	s[0] = 0;
	for (int i = 1; i < n; i++)
	    s[i] = s[i-1] + (y[i]+y[i-1])*(x[i]-x[i-1])/2;


	cout.precision(12);
	const double eps = 1e-9;

	for (int i = 1; i < g; i++) {
	    double target = i*s[n-1]/g;

	    int j = 1;
	    while (s[j] < target+eps)
		j++;
	    target -= s[j-1];

	    if (target < eps) {
		cout << x[j-1] << endl;
		continue;
	    }
	    
	    double k = (y[j]-y[j-1])/(x[j]-x[j-1]);
	    double d = 0;
	    double h = x[j]-x[j-1];


	    while (h-d > eps) {
		double t = (h+d)/2;
		if ((y[j-1]+k*t/2)*t < target)
		    d = t;
		else
		    h = t;
	    }

	    cout << x[j-1]+d << endl;
	}
    }
}
