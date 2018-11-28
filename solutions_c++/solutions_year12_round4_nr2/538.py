#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
template <typename T> inline bool checkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template <typename T> inline bool checkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long lint;

const int MAXN = 10 + 5;

lint r[MAXN];
double x[MAXN], y[MAXN];
int n, w, l;

double get_rand(int range) {
    double ans = 0.0;
    for (int tim = 0; tim < 3; ++tim) {
        int tmp = rand() % range;
        ans = ans + tmp;
    }
    return ans / 10;
}

inline bool check(int i) {
    for (int j = 0; j < i; ++j) {
        double dx = x[i] - x[j], dy = y[i] - y[j];
        double dis = sqrt(dx * dx + dy * dy);
        double dd = r[i] + r[j];
        if (dis <= dd) {
            return false;
        }
    }
    return true;
}

bool dfs(int i) {
    if (i >= n) {
        return true;
    }
    x[i] = x[i - 1] + r[i - 1] + r[i] + 1e-6;
    y[i] = y[i - 1];
    if (x[i] <= w && check(i)) {
        bool tmp = dfs(i + 1);
        if (tmp) return true;
    }
    x[i] = x[i - 1];
    y[i] = y[i - 1] + r[i - 1] + r[i] + 1e-6;
    if (y[i] <= l && check(i)) {
        bool tmp = dfs(i + 1);
        if (tmp) return true;
    }
    double d = sqrt(r[i - 1] + r[i] + 1e-4);
    x[i] = x[i - 1] + d;
    y[i] = y[i - 1] + d;
    if (x[i] <= w && y[i] <= l && check(i)) {
        bool tmp = dfs(i + 1);
        if (tmp) return true;
    }
    return false;
}

int main() {
    freopen("B.out", "w", stdout);
    srand(time(0));
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        out(t);
        scanf("%d%d%d", &n, &w, &l);
        REP(i, n) {
            scanf("%I64d", r + i);
        }
        x[0] = 0; y[0] = 0;
        //x[1] = w; y[1] = l;
        while (true) {
            if (dfs(1)) break;
        }
        printf("Case #%d:", t);
        REP(i, n) {
            printf(" %.2lf %.2f", x[i], y[i]); 
        }
        puts("");
    }
    return 0;
}

