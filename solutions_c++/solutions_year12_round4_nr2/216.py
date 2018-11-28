#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;


const double INF = 1000000;
const double EPS = 1E-6;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
    	int n, w, l;
    	cin >> n >> w >> l;
    	vector<pair<int, int> > balls(n);
    	for (int i =0 ; i< n; ++i) {
    		balls[i].second = i;
    		cin >> balls[i].first;
    	}
    	sort(all(balls));
    	reverse(all(balls));

    	stack< pair< pair<int, int>, pair<int, int> > > rects;
    	rects.push(mp(mp(-INF, -INF), mp(w + INF, l + INF)));
    	vector<int> xx(n), yy(n);

    	for (int i = 0; i < n; ++i) {
			int r = balls[i].first;
    		bool ok = false;
    		while (!ok) {
    			assert(!rects.empty());
    			pair< pair<int, int>, pair<int, int> > rect = rects.top();
    			rects.pop();
    			int x1 = rect.first.first, y1 = rect.first.second,x2 = rect.second.first, y2 = rect.second.second;
    			int x = max(0, x1 + r), y = max(0, y1 + r);
    			if (x > w || y > l || x + r > x2 || y + r > y2)
    				continue;
    			xx[balls[i].second] = x;
    			yy[balls[i].second] = y;
    			ok = true;
    			if (x2 - x < y2 - y) {
					rects.push(mp(mp(x + r, y1), mp(x2, y + r)));
					rects.push(mp(mp(x1, y + r), mp(x2, y2)));
    			} else {
    				rects.push(mp(mp(x1, y + r), mp(x + r, y2)));
    				rects.push(mp(mp(x + r, y1), mp(x2, y2)));
    			}
    		}
    	}


		//printf("Case #%d: %.6lf\n", testNumber, res);
    	cout << "Case #" << testNumber << ":";
    	for (int i = 0; i < n; ++i) {
    		cout << " " << xx[i] << " " << yy[i];
    	}


    	cout << endl;
    }

    return 0;
}
