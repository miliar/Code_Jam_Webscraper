/*
 * File:   C.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月7日, 下午8:04
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

int t, minv, val, n, sum;

int Solve() {
    scanf("%d", &n);
    val = 0, sum = 0;
    for (int i = 0, a; i < n; i++) {
        scanf("%d", &a);
        if (i == 0) minv = a;
        else minv = min(minv, a);
        sum += a;
        val ^= a;
    }
    if (val != 0) {
        puts("NO");
    } else {
        printf("%d\n", sum - minv);
    }
    return 0;
}

int main() {

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++cas);
        Solve();
    }
    return 0;
}
