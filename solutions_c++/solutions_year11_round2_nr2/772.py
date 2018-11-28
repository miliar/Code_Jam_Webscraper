/*
 * File:   B.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月22日, 上午1:34
 */

#include <algorithm>
#include <iostream>
#include <utility>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
using namespace std;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef long long LL;

const double EPS = 1e-4;

const int MAXN = 220;
int n, d, pos[MAXN], cnt[MAXN], tmp[MAXN];

bool Dif(double tim) {
    double last = -(1e10);
    for (int i = 0; i < n; ++i) {
        tmp[i] = cnt[i];
        while (tmp[i]>0) {
            --tmp[i];
            if (last + d < pos[i]) {
                last = max(last + d, pos[i] - tim);
            } else if (pos[i] + tim < last + d) {
                return false;
            } else {
                last = last + d;
            }
        }
    }
    return true;
}

int Solve() {
    scanf("%d %d", &n, &d);
    for (int i = 0; i < n; ++i) scanf("%d %d", &pos[i], &cnt[i]);
    double L = 0.0, R = 1e10;
    while (L + EPS < R) {
        double mid = (L+R)/2;
        if (Dif(mid)) R = mid;
        else L = mid;
    }
    printf("%.1f\n", L);
    return 0;
}

int main() {

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++cas);
        Solve();
    }
    return 0;
}
