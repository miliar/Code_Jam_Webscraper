#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

double solve() {
    int x, walk, run, t, n;
    cin >> x >> walk >> run >> t >> n;
    double T = t;
    vector<PII> v;
    int start = 0;
    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a > start) {
            v.PB(PII(0, a - start));
        }
        v.PB(PII(c, b - a));
        start = b;
    }
    if (start < x) {
        v.PB(PII(0, x - start));
    }
    sort(v.begin(), v.end());
    double ret = 0;
    for (int i = 0; i < (int)v.size(); i++) {
        int v1 = v[i].FI;
        double s1 = v[i].SE;
        if ((v1 + run) * T >= s1) {
            double t2 = s1 / (v1 + run);
            T -= t2;
            ret += t2;
        }
        else {
            if (T > 0) {
                double s2 = T * (v1 + run);
                ret += T;
                s1 -= s2;
                T = 0;
            }
            double t2 = s1 / (v1 + walk);
            ret += t2;
        }
//        printf("%d %d %d %lf %lf %lf\n", v[i].FI, v[i].SE, v1, s1, T, ret);
    }
    return ret;
}

int main()
{
//    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        double ret = solve();
        printf("Case #%d: %.10f\n", u, ret);
//        cout << "Case #" << u << ": " << ret << "\n";
    }
}

