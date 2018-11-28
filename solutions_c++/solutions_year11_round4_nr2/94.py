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

char a[550][550];
PLL b[550][550];
lint s[550][550];
PLL c[550][550];

void solve() {
    int n, m, d;
    scanf("%d%d%d", &n, &m, &d);
    for (int i = 0; i < n; ++i) {
        scanf("%s", a[i]);
        for (int j = 0; j < m; ++j) {
            a[i][j] -= '0';
            b[i][j] = PLL(i, j) * lint(a[i][j]);
        }
    }
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            c[i][j] = i && j ? c[i - 1][j] + c[i][j - 1] - c[i - 1][j - 1] + b[i - 1][j - 1] : PLL();
        }
    }
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            s[i][j] = i && j ? s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i - 1][j - 1] : 0;
        }
    }
    for (int k = min(n, m); k >= 3; --k) {
        for (int i = 0; i <= n - k; ++i) {
            for (int j = 0; j <= m - k; ++j) {
                lint sm = s[i + k][j + k] + s[i][j] - s[i][j + k] - s[i + k][j] - a[i][j] - a[i + k - 1][j] - a[i][j + k - 1] - a[i + k - 1][j + k - 1];
                PLL cm = (c[i + k][j + k] + c[i][j] - c[i][j + k] - c[i + k][j] - b[i][j] - b[i + k - 1][j] - b[i][j + k - 1] - b[i + k - 1][j + k - 1]) * 2LL;
                PLL cm1 = PLL(i * 2 + k - 1, j * 2 + k - 1) * sm;
                if (cm1 == cm) {
                    printf("%d\n", k);
                    return;
                }
            }
        }
    }
    printf("IMPOSSIBLE\n");
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
