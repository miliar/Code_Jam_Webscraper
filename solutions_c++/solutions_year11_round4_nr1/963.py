/*
 * Author: Dumbear
 * Created Time:  2011/6/4 21:50:55
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

const double eps = 1e-12;

struct Way {
    double s, t, w;
    Way() {
    }
    Way(double _s, double _t, double _w): s(_s), t(_t), w(_w) {
    }
};

bool operator<(const Way& w1, const Way& w2) {
    return w1.w < w2.w;
}

double x, s, r, t;
int tt, n;
Way way[1024];

void solve();

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
    vector<Way> way;
    double last = 0;
    for (int i = 0; i < n; ++i) {
        Way tmp;
        scanf("%lf%lf%lf", &tmp.s, &tmp.t, &tmp.w);
        way.push_back(tmp);
        if (tmp.s > last + eps) {
            way.push_back(Way(last, tmp.s, 0));
        }
        if (i == n - 1 && x > tmp.t + eps) {
            way.push_back(Way(tmp.t, x, 0));
        }
        last = tmp.t;
    }
    sort(way.begin(), way.end());
    double ans = 0;
    double rem = t;
    for (int i = 0; i < way.size(); ++i) {
        double l = way[i].t - way[i].s;
        if (l / (r + way[i].w) < rem + eps) {
            rem -= l / (r + way[i].w);
            ans += l / (r + way[i].w);
        } else {
            ans += rem + (l - rem * (r + way[i].w)) / (s + way[i].w);
            rem = 0;
        }
    }
    printf("Case #%d: %.10lf\n", ++tt, ans);
}
