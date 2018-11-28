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
        int k;
        cin >> k;
        
        int x = 1, y = 1;
        int dx = 0, dy = 0;
        int res = 0;
        for (int i = 0; i < k; ++i) {
            char c;
            int a;
            cin >> c >> a;
            if (c == 'O') {
                int time = max(abs(y - a) - dy, 0) + 1;
                res += time;
                dy = 0;
                dx += time;
                y = a;
            } else {
                int time = max(abs(x - a) - dx, 0) + 1;
                res += time;
                dx = 0;
                dy += time;
                x = a;
            }
        }
        cout << "Case #" << t + 1 << ": " << res << endl;
    }


    return 0;
}

