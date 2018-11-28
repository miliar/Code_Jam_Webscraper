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
    
    vector<bool> notprime(1000000);
    vector<int> primes;
    for (int k = 2; k < 1000000; ++k) {
        if (notprime[k]) continue;
        primes.pb(k);
        if (k <= 1000000 / k) {
            for (int l = k * k; l < 1000000; l += k) {
                notprime[l] = true;
            }
        }
        /*if (sz(primes) % 1000 == 0) {
            cerr << k << endl;
        }*/
    }
    cerr << "done: " << sz(primes) << endl;

    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int64 n;
        cin >> n;
        int64 res;
        if (n == 1) res = 0;
        else {
            res = 1;
            for (int i = 0; i < sz(primes); ++i) {
                int p = primes[i];
                int64 pp = 1;
                int d = 0;
                while (pp <= n / p) {
                    pp *= p;
                    ++d;
                }
                if (d <= 1) break;
                res += d - 1;
            }
        }
        cout << "Case #" << tt << ": " << res << endl;
    }

    return 0;
}
