#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
using namespace std;
#define MP make_pair
#define PB push_back
#define MAXN 10005
int n, D;
pair<int, int> v[MAXN];
bool yes;

void dfs(int cur, int l, int d) {
    if (cur + 2 * l >= D) yes = 1;
    if (yes) return;
    for (int i = d + 1; v[i].first - cur <= 2 * l && i <= n; i++) {
        int nl = min(v[i].first - cur - l, v[i].second);
        dfs(v[i].first - nl, nl, i);
    }
}

int main() {
    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);
    int cas, cass = 0;
    cin >> cas;
    while (cas--) {
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> v[i].first >> v[i].second;
        cin >> D;
        sort(v + 1, v + n + 1);
        yes = 0;
        dfs(0, min(v[1].first, v[1].second), 1);
        printf("Case #%d: ", ++cass);
        if (yes) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}