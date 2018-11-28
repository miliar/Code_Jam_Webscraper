#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
#define forn(i, n) for (int i = 0; i < (n); i++)
#define foreach(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define eprintf(...) {fprintf(stderr,__VA_ARGS__);fflush(stderr);}
typedef pair<int, int> ii;
typedef long long LL;

int main() {
    
    int tests;
    scanf("%d\n", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d: ", test);
        int X, S, R, n;
        double t;
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &n);
        vector<ii> v;
        int walk = X;
        forn(i, n) {
            int x, y, z;
            scanf("%d%d%d", &x, &y, &z);
            v.push_back(ii(z, y - x));
            walk -= (y - x);
        }
        sort(v.begin(), v.end());
        double ans = 0.;
        if (t * R < walk) {
            ans += t + (walk - t * R) * 1. / S;
            t = 0;
        } else {
            double tt = walk * 1. / R;
            ans += tt;
            t -= tt;
        }
        foreach(it, v) {
            if (t * (R + it->first) < it->second) {
                ans += t + (it->second - t * (R + it->first)) * 1. / (S + it->first);
                t = 0;
            } else {
                double tt = it->second * 1. / (R + it->first);
                ans += tt;
                t -= tt;
            }
        }
        printf("%.9lf\n", ans);
    }
    
    return 0;
}
