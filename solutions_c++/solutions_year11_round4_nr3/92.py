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

const int dim = 1100000;
char isp[dim];
int pn;
lint p[dim];

void solve() {
    lint n;
    scanf("%Ld", &n);
    int ans = 1;
    if (n == 1) {
        ans = 0;
    } else {
        for (int i = 0; p[i] * p[i] <= n; ++i) {
            lint c = n;
            while (c >= p[i]) {
                ++ans;
                c /= p[i];
            }
            --ans;
        }
    }
    printf("%d\n", ans);
}

void init() {
    for (int j = 0; j < dim; ++j) {
        isp[j] = 1;
    }
    isp[0] = isp[1] = 0;
    pn = 0;
    for (int i = 0; i < dim; ++i) {
        if (isp[i]) {
            p[pn++] = i;
            for (int j = i * 2; j < dim; j += i) {
                isp[j] = 0;
            }
        }
    }
}

int main() {
    init();
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
