#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define N 1005

int n;
int l[N], p[N];
int c[N];

bool cmp(int l, int r) {
    if (p[l] != p[r])
        return p[l] > p[r];
    return l < r;
}

void solve() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &l[i]);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &p[i]);
    for (int i = 1; i <= n; ++i)
        c[i] = i;
    sort(c + 1, c + n + 1, cmp);
    for (int i = 1; i <= n; ++i)
        printf(" %d", c[i] - 1);
    puts("");
}

int main() {
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:", ++cas);
        solve();
    }
    return 0;
}
