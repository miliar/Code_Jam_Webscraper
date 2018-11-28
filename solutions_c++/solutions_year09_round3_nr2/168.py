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
#include <limits>
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
#define push_back pb
#define make_pair mp

const double EPS = 1e-12;

struct xyz {
    double x, y, z;
};

inline xyz sum(xyz a, xyz b) {
    xyz ret;
    ret.x = a.x + b.x;
    ret.y = a.y + b.y;
    ret.z = a.z + b.z;
    return ret;
}
inline xyz div(xyz a, double lambda) {
    xyz ret;
    ret.x = a.x / lambda;
    ret.y = a.y / lambda;
    ret.z = a.z / lambda;
    return ret;
}

inline double dot(xyz &a, xyz &b) {
    double ret = 0;
    ret += a.x * b.x;
    ret += a.y * b.y;
    ret += a.z * b.z;
    //cout << ret << endl;
    return ret;
}

inline xyz getXyz() {
    xyz ret;
    cin >> ret.x >> ret.y >> ret.z;
    return ret;
}

int main() {
    int t;
    cin >> t;
    rep(I,t) {
        int n;
        cin >> n;
        xyz x0 = {0, 0, 0}, vg = {0, 0, 0};
        rep(i,n) {
            x0 = sum(x0, getXyz());
            vg = sum(vg, getXyz());
        }
        x0 = div(x0, n);
        vg = div(vg, n);
        if (dot(vg,vg) == 0.0) {
            printf("Case #%d: %.8lf %.8lf\n", I+1, sqrt(dot(x0,x0)), 0.0);
            continue;
        }
        double a = dot(vg, x0);
        if (a > 0) {
            printf("Case #%d: %.8lf %.8lf\n", I+1, sqrt(dot(x0,x0)), 0.0);
        } else {
            double d = sqrt(-(dot(vg,x0)*dot(vg,x0)/dot(vg,vg)) + dot(x0,x0)), t = -dot(vg,x0)/dot(vg,vg);
            if (isnan(d)) d = 0.0;
            if (t < EPS) t = 0.0; 
            printf("Case #%d: %.8lf %.8lf\n", I+1, d, t);
        }
    }
    return 0;
}

