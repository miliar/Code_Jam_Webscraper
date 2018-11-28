#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>

using namespace std;

const double eps = 1e-8;

int Len, S, R, am, n, beg[1001], en[1001], w[1001];
int idx[1001];

bool cmp(int a, int b) {
    return w[a] < w[b] || w[a] == w[b] && beg[a] < beg[b];
}

double getTime(double A, int B) {
    return (double) A / (double) B;
}

void solve() {
    scanf("%d%d%d%d%d", &Len, &S, &R, &am, &n);
    int tot = Len;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d%d", beg + i, en + i, w + i);
        idx[i] = i;
        tot -= en[i] - beg[i];
    }
    sort(idx, idx + n, cmp);
    double ret = 0;
    double _am = am;
    double tt = getTime(tot, R);
    if (tt > _am + eps) {
        double dd = _am * R;
        double lef = 1. * tot - dd;
        ret += _am + getTime(lef, S);    
        _am = 0;
    } else {
        ret += tt;
        _am -= tt;
    }
    for (int i1 = 0; i1 < n; ++i1) {
        int i = idx[i1];
        int dst = en[i] - beg[i];
        tt = getTime(dst, R + w[i]);
        if (tt > _am + eps) {
            double dd = _am * (R + w[i]);
            double lef = 1. * dst - dd;
            ret += _am;
            ret += getTime(lef, S + w[i]);
            _am = 0;
        } else {
            ret += tt;
            _am -= tt;
        }
    }
    printf("%.8lf\n", ret);
}

int T;
    
int main(int argc, char** argv) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}


