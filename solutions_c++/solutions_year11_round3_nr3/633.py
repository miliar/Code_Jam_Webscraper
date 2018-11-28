/*
 * Author: Xay
 * Created Time:  2011/5/22 17:53:17
 * File Name: c.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
typedef long long lint;
const int maxint = -1u>>1;
const int mm = 100000000;
int prime[mm / 10], len;
bool used[mm];
const int maxn = 10000 + 4;
const lint MAX = 10000000000000000LL;

int n;
lint low, high;
lint a[maxn];
lint gcd[maxn];
int qn[100];
lint num[100];
int k;

lint __lcm(lint a, lint b) {
    lint g = __gcd(a, b);
    return a / g * b;
}

void initprime() {
    memset(used, 0, sizeof(used));
    prime[0] = 2;
    len = 1;
    for (int i = 3; i < mm; i += 2) {
        if (used[i]) continue;
        prime[len++] = i;
        if ((lint)i * i >= mm) continue;
        for (int j = i * i; j < mm; j += i + i) used[j] = true;
    }
    //printf("%d\n", len);
}

void find(lint &ans, lint low, lint high, lint now) {
    lint x1 = low / now, x2 = high / now;
    if (low % now) ++x1;
    //printf("%I64d %I64d %I64d %I64d: %I64d %I64d\n", low, high, now, limit, x1, x2);
    lint res = -1;
    if (x1 <= x2) res = x1 * now;
    if (res == -1) return;
    if (ans < 0 || ans > res) ans = res;
}

void dfs(lint now, int dep, const lint &low, const lint &high, lint &res) {
    if (now > high) return;
    if (low <= now && now <= high) {
        res = min(res, now);
        return ;
    }
    if (dep >= k) return;
    dfs(now, dep + 1, low, high, res);
    for (int i = 0; i < qn[dep]; ++i) {
        now *= num[dep];
        dfs(now, dep + 1, low, high, res);
    }
}

void find(lint &ans, lint low, lint high, lint now, lint limit) {
    k = 0;
    for (int i = 0; i < len && (lint)prime[i] * prime[i] <= limit; ++i) {
        if (limit % prime[i] == 0) {
            qn[k] = 0;
            num[k] = prime[i];
            while (limit % prime[i] == 0) {
                limit /= prime[i];
                ++qn[k];
            }
            ++k;
        }
    }
    if (limit > 1) {
        qn[k] = 1;
        num[k++] = limit;
    }
    //for (int i = 0; i < k; ++i) {
        //printf("%I64d: %d\n", num[i], qn[i]);
    //}
    lint x1 = low / now, x2 = high / now;
    if (low % now) ++x1;
    lint res = MAX;
    dfs(1, 0, x1, x2, res);
    if (x1 <= res && res <= x2) {
        if (ans < 0 || ans > res * now) ans = res * now;
    }
}

int main() {
    initprime();
    //return 0;
    freopen("c.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        scanf("%d%I64d%I64d", &n, &low, &high);
        for (int i = 0; i < n; ++i) {
            scanf("%I64d", &a[i]);
        }
        sort(a, a + n);
        gcd[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            gcd[i] = __gcd(a[i], gcd[i + 1]);
        }
        lint now = 1, ans = -1;
        for (int i = 0; i < n; ++i) {
            if (gcd[i] % now == 0) {
                find(ans, low, high, now, gcd[i] / now);
                //break;
            }
            now = __lcm(now, a[i]);
            if (now % a[i]) break;
        }
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            if (now % a[i]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            find(ans, low, high, now);
        }
        if (ans < 0) printf("NO\n");
        else printf("%I64d\n", ans);
    }
    return 0;
}

