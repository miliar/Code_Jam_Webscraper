#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>

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

int p[200];
int v[200];

int main() {
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {

	int c, d;
	cin >> c >> d;
	REP(i, c)
	    cin >> p[i] >> v[i];

	double low = 0;
	double high = 1e14;
	while (high-low > 1e-1) {
	    double s = (low+high)/2;
	    double last = -1e10;
	    bool ok = true;
	    REP(i, c) {
		last = max(p[i]-s, last+d)+d*(v[i]-1);
		if (last-p[i] > s) {
		    ok = false;
		    break;
		}
	    }
	    if (ok) 
		high = s;
	    else
		low = s;
	}

	double res  = round(low+high)/2;
	printf("Case #%d: %0.1lf\n", cs, res);
    }
}
