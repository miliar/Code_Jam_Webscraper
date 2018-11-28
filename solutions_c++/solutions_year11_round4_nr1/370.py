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
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int X, S, R, N;
        double t;
        cin >> X >> S >> R >> t >> N;
        vector<pair<double, double> > walkways(N);
        for (int i = 0; i < N; ++i) {
            int b, e;
            cin >> b >> e >> walkways[i].x;
            walkways[i].y = e - b;
            X -= e - b;
            walkways[i].x += S;
        }
        walkways.pb(mp(S, X));
        sort(all(walkways));
        double res = 0;
        double delta = R - S;
        for (int i = 0; i < sz(walkways);++i) {
            double t1 = min(t, walkways[i].y / (walkways[i].x + delta));
            res += t1 + (walkways[i].y - t1 * (walkways[i].x + delta)) / walkways[i].x;
            t -= t1;
        }
        printf("Case #%d: %.6lf\n", tt, res);
    }

    return 0;
}
