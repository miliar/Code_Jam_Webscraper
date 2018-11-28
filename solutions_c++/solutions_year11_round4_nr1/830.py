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


using namespace std;


#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define debug(x) cout << '>' << #x << ':' << x << endl;

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)


typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;






int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int x, s, r, n;
        double tmax;
        cin >> x >> s >> r >> tmax >> n;
        int dr = r - s;
        vector < pair<int,int>  > dist;
        for (int i = 0; i < n; ++i) {
            int a, b, v;
            cin >> a >> b >> v;
            dist.pb(mp(v + s, b - a));
            x -= (b - a);
        }
        if (x > 0) dist.pb(mp(s, x));
        sort(all(dist));

        double ans = 0;
        for (int i = 0; i < sz(dist); ++i) {
            int v = dist[i].first;
            int d = dist[i].second;
            if (tmax > 0) {
                double t1 = (double) d / (v + dr);
                double trun = min(tmax, t1);
                double drun = trun * (v + dr);
                double dost = d - drun;
                double tost = dost / v;
                tmax -= trun;
                ans += trun;
                ans += tost;       
            } else {
                ans += (double) d / v;
            }
        }
        printf("Case #%d: %.9lf\n", t + 1, ans);
    }


    return 0;
}

