#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

char ch[200];
int pos[200];
int res;
int n;
int p[2], tt[2];

void solve() {
    p[0] = p[1] = 1;
    tt[0] = tt[1] = 0;
    res = 0;
    int u, v;
    for (int rt = 0; rt < n; rt++) {
        if (ch[rt] == 'O') {
            u = 0; v = 1;
        } else {
            u = 1; v = 0;
        }
        int ntime = abs(p[u] - pos[rt]);

        res = max(res, tt[u] + ntime) + 1;
        //printf("u = %d ntime = %d p[u] = %d pos[rt] = %d res = %d\n", u, ntime, p[u], pos[rt], res);
        tt[u] = res; p[u] = pos[rt];

    }
}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        rep(i, n) scanf(" %c %d", &ch[i], &pos[i]);
        solve();
        printf("Case #%d: %d\n", tt + 1, res);
    }
    return 0;
}
