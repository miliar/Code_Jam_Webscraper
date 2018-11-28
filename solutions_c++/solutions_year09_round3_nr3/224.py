#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for (iter(c) i = (c).begin(); i != (c).end(); i++)
#define inrange(x,mn,mx) (x >= mn && x < mx)
#define pb push_back
#define mp make_pair

int main() {
    int t;
    cin >> t;
    rep(I,t) {
        int n, m;
        cin >> n >> m;
        vector<int> released;
        rep(i,m) {
            int tmp;
            cin >> tmp; tmp--;
            released.pb(tmp);
        }
        // bad implementation
        int mn = 987654321;
        do {
            int calc = 0;
            rep(i,released.size()) {
                // + direction
                int cur = released[i] + 1;
                while (find(released.begin(), released.begin()+i, cur) == released.begin()+i && cur < n) {
                    cur++;
                    calc++;
                }
                // - direction
                cur = released[i] - 1;
                while (find(released.begin(), released.begin()+i, cur) == released.begin()+i && cur >= 0) {
                    cur--;
                    calc++;
                }
            }
/*            if (mn > calc) {
                //printf("current min: %d\n", calc);
                //rep(i,released.size()) cout << released[i] << ' '; cout << endl;
            }*/
            mn = min(mn, calc);
        } while (next_permutation(all(released)));
        printf("Case #%d: %d\n", I+1, mn);
    }
    return 0;
}

