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

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        
        int n;
        cin >> n;
        vi cards(n);
        for (int i = 0; i < n; ++i) cin >> cards[i];

        sort(all(cards));
        int res = n;
        queue<int> qu;
        int pc = 0;
        int pv = 0;

        int i = 0;
        while (i < n) {
            if (cards[i] != pv + 1) {
                while (pc > 0) {
                    int p = qu.front();
                    qu.pop();
                    res = min(res, pv + 1 - p);
                    --pc;
                }
            }
            pv = cards[i];
            int count = 1;
            while (i + count < n && cards[i + count] == cards[i]) ++count;
            while (count > pc) {
                qu.push(pv);
                ++pc;
            }
            while (count < pc) {
                int p = qu.front();
                qu.pop();
                res = min(res, pv - p);
                --pc;
            }

            i += count;
        }
        while (pc > 0) {
            int p = qu.front();
            qu.pop();
            res = min(res, pv + 1 - p);
            --pc;
        }
        /*printf("Case #%d:\n", testNumber);
        for (int i = 0; i < sz(res); ++i) {
            printf("%.8lf\n", res[i]);
        }*/
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}