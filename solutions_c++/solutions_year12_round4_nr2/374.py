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
#define MAXN 1005
int n, w, l;
pair<int, int> r[MAXN];
pair<int, pair<int, int> > ans[MAXN];

int main() {
    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);
    int cas, cass = 0;
    cin >> cas;
    while (cas--) {
        cin >> n >> w >> l;
        for (int i = 1; i <= n; i++) {
            cin >> r[i].first;
            r[i].second = i;
        }
        sort(r + 1, r + 1 + n);
        int t = -1000000000, last = -r[1].first, nt = t;
        bool lr = 0;
        for (int i = 1; i <= n; i++) {
            if (!lr) {
                if (last + r[i].first <= w) {
                    ans[i].first = r[i].second;
                    ans[i].second.first = last + r[i].first;
                    ans[i].second.second = max(t + r[i].first, 0);
                    nt = max(nt, ans[i].second.second + r[i].first);
                    last += 2 * r[i].first;
                } else {
                    lr = 1;
                    last = w + r[i].first;
                    t = nt;
                    i--;
                }
            } else {
                if (last - r[i].first >= 0) {
                    ans[i].first = r[i].second;
                    ans[i].second.first = last - r[i].first;
                    ans[i].second.second = t + r[i].first;
                    nt = max(nt, ans[i].second.second + r[i].first);
                    last -= 2 * r[i].first;
                } else {
                    lr = 0;
                    last = -r[i].first;
                    t = nt;
                    i--;
                }
            }
        }
        if (t > l) puts("wa");
        sort(ans + 1, ans + 1 + n);
        printf("Case #%d:", ++cass);
        for (int i = 1; i <= n; i++)
            printf(" %d.0 %d.0", ans[i].second.first, ans[i].second.second);
        puts("");
    }
    return 0;
}