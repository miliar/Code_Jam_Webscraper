/*
 * Author: xay
 * Created Time:  2010-5-8 19:34:39
 * File Name: c.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
const int maxn = 1000 + 5;

typedef long long lint;
int r, k, n;
int g[maxn];
pair<int, lint> used[maxn];

int next(int r, int n) {
    if (r + 1 == n) return 0;
    return r + 1;
}
lint go(int r, int &pos) {
    lint res = 0;
    while (r--) {
        lint num = g[pos], nxt = next(pos, n);
        while (nxt != pos && num + g[nxt] <= k) {
            num += g[nxt];
            nxt = next(nxt, n);
        }
        res += num;
        pos = nxt;
    }
    return res;
}
pair<int, lint> cal_time() {
    memset(used, 0, sizeof(used));
    int pos = 0, cnt = 1;
    lint sum = 0;
    while (!used[pos].first) {
        used[pos].first = cnt++;
        used[pos].second = sum;
        sum += go(1, pos);
    }
    return make_pair(cnt - used[pos].first, sum - used[pos].second);
}
int main() {
    freopen("c.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        scanf("%d%d%d", &r, &k, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
        }
        pair<int, lint> time = cal_time();
//        printf("%d %d\n", time.first, time.second);
        lint ans;
        int pos = 0;
        if (r < n) {
            ans = go(r, pos);
        } else {
            r -= n;
            ans = go(n, pos);
            ans += time.second * (r / time.first);
            r %= time.first;
            ans += go(r, pos);
        }
        printf("%I64d\n", ans);
    }
    return 0;
}

