/*
 * Author: Xay
 * Created Time:  2011/5/7 12:55:28
 * File Name: a.cpp
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
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int n;
        scanf("%d", &n);
        int ta = 0, tb = 0, pa = 1, pb = 1;
        int t = 0;
        char s[3];
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%s%d", s, &x);
            if (s[0] == 'O') {
                ta += abs(x - pa) + 1;
                ta = max(ta, t + 1);
                t = max(t, ta);
                pa = x;
            } else if (s[0] == 'B') {
                tb += abs(x - pb) + 1;
                tb = max(tb, t + 1);
                t = max(t, tb);
                pb = x;
            }
        }
        printf("%d\n", t);
    }
    return 0;
}

