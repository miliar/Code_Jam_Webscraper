#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

//#define mp make_pair
#define pb push_back
#define ll long long
#define va vector<int>
#define left l1
#define right r1
#define sgn(x) (x < 0 ? -1 : 1)

const int maxn = 1000, n = 6;

string ls, s;
struct wh{
    long double a, b, c;
    friend bool operator < (const wh& a, const wh& b) {
        return a.c < b.c;
    }
};

vector <wh> be;

int main() {
    int T, n;
    long double x, s, r, t, b, e, w;
    cin >> T;
    for (int ff = 1; ff <= T; ++ff) {
        cin >> x >> s >> r >> t >> n;
        be.resize(n);
        long double res, f = x, px;
        res = t;
        
        for (int i = 0; i < n; ++i) {
            cin >> be[i].a >> be[i].b >> be[i].c;
//            res += (e - b) / (w + s);
            f -= be[i].b - be[i].a;
        }
        be.pb(be[0]);
        be[be.size() - 1].a = be[be.size() - 1].c = 0;
        be[be.size() - 1].b = f;
        sort(be.begin(), be.end());
        res = 0;
        int ost = t;
        for (int i = 0; i < be.size(); ++i) {
            if (t >= (be[i].b - be[i].a) / (be[i].c + r)) {
                res += (be[i].b - be[i].a) / (be[i].c + r);
                t -= (be[i].b - be[i].a) / (be[i].c + r);
            } else {
                px = t * (be[i].c + r);
                res += t + (be[i].b - be[i].a - px) / (be[i].c + s);
                t = 0;
            }
        }
        //cout << "now res is " <<res << endl; 
        cout.precision(20);
        cout << "Case #" << (ff) << ": " << res << endl;
    }
}
