#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <functional>
#include <complex>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); ++i)
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()

const int inf = 987654321;
const double eps = 1e-9;

int main() {
    int T;
    cin >> T;
    rep(I,T) {
        int n;
        cin >> n;
        char a[200][200], b[200][200];
        
        memset(a,0,sizeof(a)); memset(b,0,sizeof(b));
        rep(i,n) {
            int x,y,z,w;
            cin >> x >> y >> z >> w;
            for (int i = x; i <= z; ++i) for (int j = y; j <= w; ++j) a[i][j] = 1;
        }
        
        int ans = 0;
        for (;;) {
            rep(i,200) rep(j,200) b[i][j] = a[i][j];
            bool fin = true;
            rep(i,200) rep(j,200) if (a[i][j]) fin = false;
            if (fin) break;
            rep(i,200) rep(j,200) if (i > 0 && j > 0) {
                if (!a[i][j-1] && !a[i-1][j]) b[i][j] = 0;
                if (a[i][j-1] && a[i-1][j]) b[i][j] = 1;
            }
            rep(i,200) rep(j,200) a[i][j] = b[i][j];
            ++ans;
        }
        
        cout << "Case #" << I+1 << ": " << ans << endl;
    }
    return 0;
}

