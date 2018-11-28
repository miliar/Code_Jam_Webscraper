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

PII a[1100];

void solve() {
    int x, s, r, t, n;
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    r -= s;
    for (int i = 0; i < n; ++i) {
        int b, e, v;
        scanf("%d%d%d", &b, &e, &v);
        a[i] = mp(v + s, e - b);
        x -= e - b;
    }

    a[n++] = mp(s, x);
    sort(a, a + n);
    double left = t;
    double tim = 0;
    for (int i = 0; i < n; ++i) {
        double use = min(left, 1.0 * a[i].Y / (a[i].X + r));
        left -= use;
        tim += (a[i].Y - use * r) / a[i].X;
    }
    printf("%.7lf\n", tim);
}

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    cin >> n;
    for (int test = 1; test <= n; ++test) {
//        printf("Case #%d:\n", test);
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
