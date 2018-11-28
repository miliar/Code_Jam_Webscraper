#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset((a),(b),sizeof(a))

#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

const string fileName = "A-large";

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int t;
    cin >> t;
    FOR (test, 1, t+1) {
        int x, s, r, _t, n;
        cin >> x >> s >> r >> _t >> n;
        vector <pair <int, int> > a (n);
        int xx, yy;
        REP (i, n) {
            cin >> xx >> yy >> a[i].X;
            a[i].Y = yy-xx;
            a[i].X += s;
            x -= a[i].Y;
        }
        a.pb (make_pair (s, x));
        sort(all(a));
        r-=s;
        double t = _t;
        double res = 0.0;
        REP (i, sz (a)) {            
            if (t * (a[i].X + r) >= a[i].Y) {
                t -= (double) a[i].Y / (a[i].X + r);
                res += (double) a[i].Y / (a[i].X + r);
            } else {
                res += t + (double) (a[i].Y - t * (a[i].X + r)) / a[i].X;
                t = 0;
            }
        }
        printf ("Case #%d: %.9lf\n", test, res);
    }
	return 0;
}
