#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 10000 + 10;

int d[maxn], l[maxn], n, D;
bool mark[maxn];

int f[maxn];

void main2() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", d+i, l+i);
    }
    scanf("%d", &D);

    /*
    memset(mark, false, sizeof mark);

    set<pair<int, int> > mini;
    set<pair<int, int> > maxi; 
    int ptr = 1;
    int cur = d[0], now = d[0] + min(d[0], l[0]);
    while (true) {
        if (now >= D) {
            printf("YES\n");
            return;
        }
        while (ptr < n && d[ptr] <= now) {
            maxi.insert(make_pair(l[ptr] + d[ptr], ptr));
            mini.insert(make_pair(d[ptr] - l[ptr], ptr));
            ptr++;
        }
        while (mini.size() > 0 && (mini.begin()->first < cur)) {
            int id = mini.begin()->second;
            if (!mark[id]) {
                mark[id] = true;
                maxi.erase(make_pair(l[id] + d[id], id));
                maxi.insert(make_pair(d[id] - cur + d[id], id));
            }
            mini.erase(mini.begin());
        }
        if (maxi.size() > 0) {
            set<pair<int, int> >::iterator it = maxi.end();
            it--;
            if (it->first <= now) break;
            mark[it->second] = true;
            cur = d[it->second];
            now = it->first;
            maxi.erase(it);
        } else {
            break;
        }
    }
    printf("NO\n");
    */
    for (int i = 0; i < n; ++i) f[i] = 0;
    f[0] = min(l[0], d[0]);
    for (int i = 0; i < n; ++i) {
        if (d[i] + f[i] >= D) {
            printf("YES\n");
            return;
        }
        for (int j = i + 1; j < n; ++j) {
            if (d[j] <= d[i] + f[i]) {
                f[j] = max(f[j], min(l[j], d[j] - d[i]));
            }
        }
    }
    printf("NO\n");
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A.out", "w", stdout);
    //freopen("A-small-attempt0.out", "w", stdout);
    //freopen("A.in", "r", stdin);
    int T, ca = 0;
    for (scanf("%d", &T); T--; ) {
        printf("Case #%d: ", ++ca);
        main2();
    }
}

