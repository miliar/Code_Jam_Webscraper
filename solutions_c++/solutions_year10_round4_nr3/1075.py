#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 100 + 10;
const int inf = (-1u) >> 1;

int Case = 1, maxx, maxy, n;
bool m[maxn][maxn], now[maxn][maxn];

void paint(int a, int b, int c, int d) {
    for (int i = b; i <= d; ++i)
        for (int j = a; j <= c; ++j)
            m[i][j] = true;
}

void init() {
    scanf ("%d", &n);
    maxx = 0, maxy = 0;
    memset (m, false, sizeof(m));
    for (int i = 0, a, b, c, d; i < n; ++i) {
        scanf ("%d%d%d%d", &a, &b, &c, &d);
        maxx = max(c, maxx);
        maxy = max(d, maxy);
        paint(a, b, c, d);
    }
}

void change() {
    for (int i = 0; i <= maxy; ++i)
        for (int j = 0; j <= maxx; ++j) {
            if ((i == 0 || !m[i - 1][j]) &&
                (j == 0 || !m[i][j - 1]))
                now[i][j] = false;
            else if ((i != 0 && m[i - 1][j]) && 
                    (j != 0 && m[i][j - 1])) 
                now[i][j] = true;
        }
}

bool find() {
    memcpy (now, m, sizeof(m));
    bool flag = false;
    for (int i = 0; i <= maxy; ++i)
        for (int j = 0; j <= maxx; ++j)
            if (m[i][j]) {
                flag = true; break;
            }
    if (!flag) return false;
    change(); return true;
}

void solve() {
    printf ("Case #%d: ", Case++);
    int ans = 0;
    while (find()) {
        ++ans;
        memcpy (m, now, sizeof(now));
    }
    printf ("%d\n", ans);
}

#define SMALL
//#define LARGE

int main() {
    string name = "C";
    #ifdef SMALL
    freopen ((name + "-small-attempt0.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}

