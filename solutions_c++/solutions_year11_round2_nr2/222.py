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


typedef pair <int64, int64> pii;
typedef vector < pii > vpii;


const double EPS = 1e-7;

bool check(const vpii & v, int64 d, long double tm) {
    long double now = v[0].first - tm;

    for (int i = 0; i < sz(v); ++i) {
        now = max(now, v[i].first - tm);
        long double last = now + (v[i].second - 1) * d;
        if (last > v[i].first + tm) return false;
        now = last + d;
    }

    return true;
}



int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    
    int T;
    cin >> T;

    for (int nt = 0; nt < T; ++nt) {
        int d, n;
        cin >> n >> d;
        vpii v;
        for (int i = 0; i < n; ++i) {
            int p, num;
            cin >> p >> num;
            v.pb(mp(p, num));
        }
        

        long double hi = 1e18;
        long double lo = 0;
        
        while (hi - lo > EPS) {
            long double tm = (hi + lo) / 2;
            
            bool ok = check(v, d, tm); 
            if (ok) {
                hi = tm;
            } else {
                lo = tm;
            }

        }

         
        cout << "Case #" << nt + 1 << ": ";
        printf("%.9lf\n", (double) hi);
    } 




    return 0;
}

