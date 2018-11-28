#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

using namespace std;

struct node{
    bool color;
    int x;
} s[21];
int ct1, ct2;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, n, x, i, tt;
    char str[5];
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++) {
        memset(s, 0, sizeof(s));
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s%d", str, &x);
            if (str[0] == 'B') s[i].color = 1;
            s[i].x = x;
        }
        int t1, t2, sum1, sum2;
        t1 = t2 = 1;
        sum1 = sum2 = 0;
        bool flag = 0; //上一个是O
        for (i = 0; i < n; i++) {
            if (!s[i].color) {
                sum1 += abs(t1 - s[i].x);
                if (flag) {
                    if (sum1 <= sum2) sum1 = sum2;
                    flag = 0;
                }
                sum1++;
                t1 = s[i].x;
            } else {
                sum2 += abs(t2 - s[i].x);
                if (!flag) {
                    if (sum2 <= sum1) sum2 = sum1;
                    flag = 1;
                }
                sum2++;
                t2 = s[i].x;
            }
        }
        printf("Case #%d: %d\n", tt, max(sum1, sum2));
    }
    return 0;
}
