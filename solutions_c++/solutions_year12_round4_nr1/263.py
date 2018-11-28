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
    	int n;
    	cin >> n;
    	vector<int> d(n), l(n);
    	for (int i = 0 ; i< n; ++i) {
    		cin >> d[i] >> l[i];
    	}
    	int D;
    	cin >> D;

    	vector<int> longest(n);
    	longest[0] = d[0];
    	int j = 1;
    	for (int i = 0; i < n; ++i) {
    		while (j < n && d[i] + longest[i] >= d[j]) {
    			longest[j] = min(l[j], d[j] - d[i]);
    			++j;
    		}
    	}
    	bool res = false;
    	for (int i = 0; i < n; ++i) {
    		if (d[i] + longest[i] >= D) {
    			res = true;
    			break;
    		}
    	}

		//printf("Case #%d: %.6lf\n", testNumber, res);
    	cout << "Case #" << testNumber << ": " << (res ? "YES" : "NO") << endl;
    }

    return 0;
}
