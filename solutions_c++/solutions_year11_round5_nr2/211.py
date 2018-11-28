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

const int lim = 11000;
int a[lim];

void solve() {
    memset(a, 0, sizeof a);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        ++a[x];
    }
    int ans = lim;
    if (n == 0) ans = 0;
    else {
        for (int i = 0; i < lim - 1; ++i) {
            if (a[i] > a[i + 1]) {
                int j = i;
                while (j >= 0 && a[j]) {
                    --a[j];
                    --j;
                }
                ans = min(ans, i - j);
                --i;
            }
        }
    }
    printf("%d\n", ans);
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
        //        printf("Case #%d:\n", test);
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
