#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;
const int d[4][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};

int Case = 1, n, g;
bool blue, red;
char s[55][55], ts[55][55];

void canwin(char c) {
    if (c == 'R') red = true;
    else blue = true;
}

void show() {
    for (int i = 0; i < n; ++i)
        puts (s[i]);
    puts(" ");
}

void check() {
    for (int k = 0; k < 4; ++k) {
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                if (s[i][j] == '.')
                    continue;
                if (i - d[k][0] < n && j - d[k][1] < n &&
                    i - d[k][0] >= 0 && j - d[k][1] >= 0
                        && s[i - d[k][0]][j - d[k][1]] == s[i][j])
                    continue;
                int cnt = 1;
                while (i + cnt * d[k][0] < n && j + cnt * d[k][1] < n &&
                       i + cnt * d[k][0] >= 0 && j + cnt * d[k][1] >= 0
                        && s[i + cnt * d[k][0]][j + cnt * d[k][1]] == s[i][j])
                    ++cnt;
                if (cnt >= g)
                    canwin(s[i][j]);
        }
    }
}

void down() {
    for (int i = 0; i < n; ++i) {
        int j = n - 1;
        for (int k = n - 1; k >= 0; --k)
            if (s[k][i] != '.')
                s[j--][i] = s[k][i];
        while(j >= 0) s[j--][i] = '.';
    }
}

void rotate() {
    memcpy (ts, s, sizeof(s));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            s[i][j] = ts[n - j - 1][i];
    down();
}

void init() {
    scanf ("%d%d", &n, &g);
    for (int i = 0; i < n; ++i)
        scanf ("%s", s[i]);
}

void solve() {
    printf ("Case #%d: ", Case++);
    blue = red = false;
    check();
    rotate();
    check();
    if (red && blue) puts("Both");
    else if (red) puts("Red");
    else if (blue) puts("Blue");
    else puts("Neither");
}

//#define SMALL
#define LARGE

int main() {
    string name = "A";
    #ifdef SMALL
    freopen ((name + "-small-attempt1.in").c_str(), "r", stdin);
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

