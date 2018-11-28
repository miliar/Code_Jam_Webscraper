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
#include <bitset>
#include <numeric>
#include <valarray>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int inf = 987654321;
const double eps = 1e-9;

struct chick {
    double x0, v, t;
};

int main() {
    int T;
    cin >> T;
    rep(I,T) {
        int n, k, goal;
        double time;
        cin >> n >> k >> goal >> time;
        vector<chick> vc(n);
        rep(i,n) cin >> vc[i].x0;
        rep(i,n) cin >> vc[i].v;
        rep(i,n) vc[i].t = (goal - vc[i].x0) / vc[i].v;
        reverse(all(vc));
        int ans = 0, cnt = 0;
        vector<bool> vb;
        rep(i,n) {
            if (vc[i].t < time + eps) {
                vb.push_back(true);
                ++cnt;
                if (cnt == k) break;
            } else {
                vb.push_back(false);
            }
        }
        //cerr << "calc" << endl;
        if (cnt < k) 
            cout << "Case #" << I+1 << ": " << "IMPOSSIBLE" << endl;
        else {
            while (true) {
                rep(i,vb.size()-1) if (!vb[i] && vb[i+1]) {
                    vb[i] = true; vb[i+1] = false;
                    ++ans;
                }
                bool ok = true;
                rep(i,k) if (!vb[i]) ok = false;
                if (ok) break;
            }
            cout << "Case #" << I+1 << ": " << ans << endl;
        }
    }
    return 0;
}
