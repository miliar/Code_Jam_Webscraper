#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

const int maxn = 100 + 10;
const int inf = (-1u) >> 1;

int Case = 1, n, m;
vector <string> v[2][maxn];

void getv(char *s, int x, int type) {
    string temp;
    v[type][x].clear();
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '/') {
            int j = i + 1;
            while (s[j] != '/' && s[j] != '\0')
                temp += s[j++];
            v[type][x].push_back(temp);
            temp = "";
            i = j - 1;
        }
    }
}

void init() {
    scanf ("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        char buf[102];
        scanf ("%s", buf);
        getv(buf, i, 0);
    }
}

int comp(int x, int y, int type) {
    int res = 0;
    while (res < (int)v[type][y].size() && res < (int)v[1][x].size()) {
        if (v[type][y][res] == v[1][x][res])
            ++res;
        else 
            return res;
    }
    return res;
} 

void solve() {
    printf ("Case #%d: ", Case++);
    int ans = 0;
    for (int i = 0; i < m; ++i) {
        char buf[102];
        scanf ("%s", buf);
        getv(buf, i, 1);
        int maxcom = 0;
        for (int j = 0; j < n; ++j)
            maxcom = max(maxcom, comp(i, j, 0));
        for (int j = 0; j < i; ++j)
            maxcom = max(maxcom, comp(i, j, 1));
        ans += (int)v[1][i].size() - maxcom;
    }
    printf ("%d\n", ans);
}

//#define SMALL
#define LARGE

int main() {
    string name = "A";
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

