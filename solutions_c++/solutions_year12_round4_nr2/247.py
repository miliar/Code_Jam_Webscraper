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

int n, w, l;
vector<pair<int, int> > p;
vector<int> r;
vector<int> x, y;

int k;

void ukladaj(int w1, int w2, int l1, int l2) {

    if (k == n) 
        return;

    int xx = (w1 == 0) ? 0 : w1+r[k];
    int yy = (l1 == 0) ? 0 : l1+r[k];

    if (xx > w || yy > l)
	return;
    if (w2 < w && xx+r[k] > w2)
	return;
    if (l2 < l && yy+r[k] > l2)
	return;

    x[k] = xx;
    y[k] = yy;
    xx += r[k];
    yy += r[k];
    k++;

    if (w2-w1 < l2-l1) {
	ukladaj(xx, w2, l1, yy);
	ukladaj(w1, w2, yy, l2);
    }
    else {
	ukladaj(w1, xx, yy, l2);
	ukladaj(xx, w2, l1, l2);
    }
}

bool check() {
    REP(i, n)
	if (x[i] < 0 || x[i] > w || y[i] < 0 || y[i] > l)
	    return false;

    REP(i, n) REP(j, i) 
	if (abs(x[i]-x[j]) < r[i]+r[j] && abs(y[i]-y[j]) < r[i]+r[j])
	    return false;

    return true;
}

int main() {
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {
	cout << "Case #" << cs << ":";


	cin >> n >> w >> l;
	p.resize(n);
	REP(i, n) {
	    cin >> p[i].first;
	    p[i].second = i;
	}
	sort(p.rbegin(), p.rend());

	r.resize(n);
	REP(i, n)
	    r[i] = p[i].first;
	x.resize(n);
	y.resize(n);
	k = 0;
	ukladaj(0, w, 0, l);


	cerr << "Check #" << cs << ": " << check() << endl;
	if (k != n)
	    cerr << "   k != n" << endl;

	REP(i, n)
	    REP(j, n) 
		if (p[j].second == i) 
		    cout << " " << x[j] << " " << y[j];
	cout << endl;
    }
}
