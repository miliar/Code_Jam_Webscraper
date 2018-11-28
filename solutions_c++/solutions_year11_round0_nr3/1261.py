/*
 * Author: Xay
 * Created Time:  2011/5/7 12:35:42
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
const int maxint = -1u>>1;

int main() {
    freopen("c.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int n;
        scanf("%d", &n);
        int xsum = 0, xmin = 1000000, sum = 0;
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            xsum ^= x;
            xmin = min(xmin, x);
            sum += x;
        }
        if (xsum != 0) {
            printf("NO\n");
            continue;
        }
        printf("%d\n", sum - xmin);
    }
    return 0;
}

