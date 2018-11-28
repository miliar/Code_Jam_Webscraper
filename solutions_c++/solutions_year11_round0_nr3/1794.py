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

int n, res;
int num[2000];
int g[2][1 << 21];

void solve() {
    res = -1;
    int now = 0;
    for (int i = 0; i < n; i++) now = now^num[i];
    if (now != 0) return;

    sort(num, num + n);
    res = 0;
    for (int i = 0; i < n; i++) res += num[i];
    res -= num[0];
}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf(" %d", &num[i]);
        solve();
        printf("Case #%d: ", tt + 1);
        if (res < 0) printf("NO\n"); else printf("%d\n", res);
    }
    return 0;
}
