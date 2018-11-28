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
	int n;
	cin >> n;
	vector<int> d(n), l(n);
	int D;
	REP(i, n)
	    cin >> d[i] >> l[i];
	cin >> D;

	vector<int> a(n, 0);

	a[0] = d[0];
	bool reach = false;
	REP(i, n) {
	    if (a[i] == 0)
		break;

	    int length= min(a[i], l[i]);
	    if (D - d[i] <= length) {
		reach = true;
		break;
	    }

	    for (int j = i+1; j < n; j++) {
		int dist = d[j]-d[i];
		if (dist > length)
		    break;
		if (dist > a[j])
		    a[j] = dist;
	    }
	}

	cout << "Case #" << cs << ": ";
	if (reach)
	    cout << "YES";
	else
	    cout << "NO";
	cout << endl;

    }
}
