/* 
 * File:   B.cc
 * Author: GongZhi
 * Problem:
 * Created on 2010年5月23日, 上午12:45
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

/*
 *
 */
struct node {
    int x, v;
} data[100];
int n, k, b, t;

int ok(int x, int v) {
    x = b - x;
    int tm = x / v;
    if (x % v)tm++;
    if (tm <= t)return 1;
    else return 0;
}

bool cmp(const node a, const node b) {
    return a.x > b.x;
}

int di() {
    int ans = 0;
    int totle = 0;
    for (int i = 0; i < n; i++)totle += ok(data[i].x, data[i].v);
    if (totle < k)return -1;
    sort(data, data + n, cmp);
    int tm = 0;
    totle = 0;
    for (int i = 0; i < n; i++) {
        if (ok(data[i].x, data[i].v) == 0)tm++;
        else {
            totle++;
            ans += tm;
            if (totle >= k)break;
        }
    }
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int kases, kase = 1;
    cin >> kases;
    while (kases--) {
        cin >> n >> k >> b >> t;
        for (int i = 0; i < n; i++)cin >> data[i].x;
        for (int i = 0; i < n; i++)cin >> data[i].v;
        int ans = di();
        printf("Case #%d: ", kase++);
        if (ans == -1)printf("IMPOSSIBLE");
        else printf("%d", ans);
        printf("\n");
    }
    return 0;
}

