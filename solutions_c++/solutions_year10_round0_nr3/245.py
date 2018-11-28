/**********************************************************************
Author: Felicia
Created Time:  2010/5/8 14:50:30
File Name: roller.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;

int64 profit(int cap, int *a, int n, int times) {
    int64 *mark = new int64[n];
    int *marki = new int[n];
    int ptr = 0;
    memset(mark, 0, sizeof(int64) * n);
    memset(marki, 0, sizeof(int) * n);
    int64 ret = 0;
    int64 circle = 0;
    int circle_len = 0;
    for (int i = 0; i < times; ) {
        int64 tcap = 0;
        int tcnt = 0;
        while (tcap + a[ptr] <= cap && tcnt < n) {
            tcnt++;
            tcap += a[ptr];
            ptr++;
            if (ptr == n) {
                ptr = 0;
            }
        }
        ret += tcap;
        i++;
        if (mark[ptr] != 0) {
            circle = ret - mark[ptr];
            circle_len = i - marki[ptr];
            ret += ((times - i) / circle_len) * circle;
            i += ((times - i) / circle_len) * circle_len;
        } else {
            mark[ptr] = ret;
            marki[ptr] = i;
        }
    }
    delete[] mark;
    delete[] marki;
    return ret;
}

int main() {
    freopen("d:\\roller.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int ca = 1;
    while (T--) {
        printf("Case #%d: ", ca++);
        int r, k, n;
        scanf("%d%d%d", &r, &k, &n);
        int *a = new int[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        int64 ret = profit(k, a, n, r);
        printf("%I64d\n", ret);
    }
    return 0;
}

