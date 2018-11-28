/*
 * File:   A.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月21日, 上午10:45
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

LL n, pd, pg;

LL Gcd(LL a, LL b) {
    if (a == 0) return b;
    return Gcd(b % a, a);
}

int Solve() {
    cin >> n >> pd >> pg;
    LL minD = 100 / Gcd(pd, 100);
    if (minD > n) {
        puts("Broken");
    } else if (pd > 0 && pg == 0) {
        puts("Broken");
    } else if (100-pd > 0 && 100-pg == 0) {
        puts("Broken");
    } else {
        puts("Possible");
    }
    return 0;
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++cas);
        Solve();
    }
    return 0;
}
