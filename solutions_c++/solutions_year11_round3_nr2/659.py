/*
 * Author: Xay
 * Created Time:  2011/5/22 17:26:07
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
typedef long long lint;
const int maxn = 1000 + 5;

int a[maxn];
int L, n, c;
lint t, ans;

void calc(int t, int &cnt, int &dis) {
    for (int i = 0; i < n; ++i) {
        int time = a[i % c] * 2;
        if (t >= time) {
            t -= time;
        } else if (t < time) {
            cnt = i;
            dis = t / 2;
            return ;
        }
    }
    cnt = n;
    dis = 0;
}

void solve(int cnt, int dis, int L) {
    vector<int> v;
    v.push_back(a[cnt % c] - dis);
    for (int i = cnt + 1; i < n; ++i) {
        v.push_back(a[i % c]);
    }
    sort(v.begin(), v.end());
    lint sum = 0;
    for (int i = 0; i < L; ++i) {
        if (v.size() - 1 - i < 0) break;
        sum += v[v.size() - 1 - i];
    }
    ans -= sum;
}

int main() {
    freopen("b.out", "w", stdout);
    int ta, ca = 0;
    scanf("%d", &ta);
    while (ta--) {
        printf("Case #%d: ", ++ca);
        scanf("%d%I64d%d%d", &L, &t, &n, &c);
        ans = 0;
        for (int i = 0; i < c; ++i) {
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < n; ++i) {
            ans += a[i % c];
        }
        ans *= 2;
        int cnt, dis;
        calc(t, cnt, dis);
        solve(cnt, dis, L);
        printf("%I64d\n", ans);
    }
    return 0;
}

