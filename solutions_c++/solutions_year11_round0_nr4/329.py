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


vector < bool > used;
vector < int > a;

int dfs(int i) {
    if (used[i]) return 0;
    used[i] = true;
    return 1 + dfs(a[i]);
}


int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int k;
        cin >> k;
        a.assign(k, 0);
        for (int i = 0; i < k; ++i) {
            cin >> a[i];
            --a[i];
        }    
        used.assign(k, false);

        int res = 0;
        for (int i = 0; i < k; ++i) {
            if (!used[i]) {
                int dd = dfs(i);
                if (dd == 1) dd = 0;
                res += dd;
            }
        }
        cout << "Case #" << t + 1 << ": " << res << endl;
    }



    return 0;
}

