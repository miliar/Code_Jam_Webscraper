/*
 * Author: momodi
 * Created Time:  2010/5/8 19:37:45
 * File Name: c.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
int n, r, k;
int dt[1010];
int next[1010];
long long bak[1010];
long long rem[1010];
int cnt[1010];

long long solve() {
    long long tot = 0;
    for (int i = 0; i < n; ++i) {
        tot += dt[i];
    }
    if (tot <= k) {
        return tot * r;
    }
    for (int i = 0; i < n; ++i) {
        int j = i;
        long long tot = 0;
        while (tot + dt[j] <= k) {
            tot += dt[j];
            j = (j + 1) % n;
        }
        next[i] = j;
        bak[i] = tot;
    }
    memset(rem, -1, sizeof(rem));
    int now = 0;
    rem[now] = 0;
    cnt[now] = 0;
    while (rem[next[now]] == -1) {
        rem[next[now]] = rem[now] + bak[now];
        cnt[next[now]] = cnt[now] + 1;
        now = next[now];
        if (cnt[now] == r) {
            return rem[now];
        }
    }
    long long ans = rem[next[now]];
    r -= cnt[next[now]];
    int rou = cnt[now] + 1 - cnt[next[now]];
    ans += (rem[now] + bak[now] - rem[next[now]]) * (r / rou);
    r = r % rou;
    while (r--) {
        now = next[now];
        ans += bak[now];
    }
    return ans;
}

int main() {
    freopen("c.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        scanf("%d %d %d", &r, &k, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", dt + i);
        }
        printf("%I64d\n", solve());
    }
    return 0;
}

