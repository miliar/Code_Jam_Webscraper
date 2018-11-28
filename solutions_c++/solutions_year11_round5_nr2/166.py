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


const int k = 10000;

int a[k], b[k], c[k];

int main() {
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {
	cout << "Case #" << cs << ": ";

	int n;
	cin >> n;

	if (n == 0) {
	    cout << 0 << endl;
	    continue;
	}

	CLEAR(a);
	REP(i, n) {
	    int x;
	    cin >> x;
	    a[x-1]++;
	}

	int d = 1;
	int h = n+1; 
	while (h-d > 1) {
	    int s = (h+d)/2;
	    bool ok = true;

	    CLEAR(b);
	    CLEAR(c);
	    REP(i, k) {
		while (b[i]+c[i] < a[i]) {
		    int j = i;
		    bool menim = false;
		    REP(q, s) {
			if (j >= k) {
			    ok = false;
			    goto out;
			}
			b[j]++;
			if (b[j] > a[j]) {
			    ok = false;
			    goto out;
			}
			if (b[j]+c[j] > a[j])
			    menim = true;
			if (menim)
			    c[j]--;
			j++;
		    }
		    if (!menim)
			while (j < k && b[j]+c[j] < a[j]) {
			    c[j]++;
			    j++;
			}
		}
	    }

out:

	    if (ok)
		d = s;
	    else
		h = s;
	}

	cout << d << endl;
    }
}
