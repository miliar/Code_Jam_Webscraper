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

#define x first
#define y second


#define debug(x) cout << '>' << #x << ':' << x << endl;



typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;





int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;
        int mn = 10000000;
        int xr = 0;
        int sm = 0;

        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            mn = min(mn, a);
            xr = xr ^ a;
            sm += a;
        } 
        cout << "Case #" << t + 1 << ": ";
        if (xr == 0) {
            cout << sm - mn << endl;
        } else {
            cout << "NO" << endl;
        }
    }


    return 0;
}

