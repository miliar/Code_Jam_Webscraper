//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
//#include <ext/hash_map>

using namespace std;
//using namespace __gnu_cxx;

#define FOR(i, a, n) for(int i=(a); i<(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define sz(X) int((X).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define all(X) (X).begin(), (X).end()

typedef long long lint;
typedef pair<int, int> PII;
typedef pair<lint, lint> PLL;
typedef pair<double, double> PDD;
typedef vector<int> VI;

template<class T> ostream &operator<<(ostream &os, vector<T> vec) {
    os << '{';

    REP(i, sz(vec)) {
        os << vec[i];
        if (i + 1 != sz(vec)) os << ',';
    }
    os << '}';
    return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, pair<T1, T2> par) {
    os << '(' << par.X << ',' << par.Y << ')';
    return os;
}

template<class T> pair<T, T> operator-(pair<T, T> p, pair<T, T> q) {
    return mp(p.X - q.X, p.Y - q.Y);
}

template<class T> pair<T, T> operator+(pair<T, T> p, pair<T, T> q) {
    return mp(p.X + q.X, p.Y + q.Y);
}

template<class T> pair<T, T> operator*(pair<T, T> p, T q) {
    return mp(p.X * q, p.Y * q);
}

double a[2][110];
double h[2][110];
double k[2][110];
int n[2];

double area(double x) {
    double ans = 0;
    for (int j = 0; j < 2; ++j) {
        double ans1 = 0;
        for (int i = 0;; ++i) {
            if (i == n[j] - 2 || a[j][i + 1] > x) {
                double y = x - a[j][i];
                ans1 += h[j][i] * y + k[j][i] * y * y / 2;
                break;
            } else {
                double y = a[j][i + 1] - a[j][i];
                ans1 += h[j][i] * y + k[j][i] * y * y / 2;
            }
        }
        if (j) ans += ans1;
        else ans -= ans1;
    }
    return ans;
}

void solve() {
    int w, g;
    scanf("%d%d%d%d", &w, &n[0], &n[1], &g);
    for (int j = 0; j < 2; ++j) {
        for (int i = 0; i < n[j]; ++i) {
            int x, y;
            scanf("%d%d", &x, &y);
            a[j][i] = x;
            h[j][i] = y;
            if (i) k[j][i - 1] = (h[j][i] - h[j][i - 1]) / (a[j][i] - a[j][i - 1]);
        }
    }
    double s = 0;
    for (int i = 0; i < g - 1; ++i) {
        s += area(w) / g;
        double l = 0, r = w;
        while (r - l > 1e-10) {
            double m = (r + l) / 2;
            if (area(m) > s) {
                r = m;
            } else {
                l = m;
            }
        }
        printf("%.9lf\n", l);
    }
}

void init() {
}

int main() {
    init();
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    cin >> n;
    for (int test = 1; test <= n; ++test) {
        printf("Case #%d:\n", test);
        //        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
