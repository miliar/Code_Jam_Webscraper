/*
 * Author: xay
 * Created Time:  2010-5-23 17:58:18
 * File Name: a.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
const int maxn = 1000 + 5;

int a[maxn], b[maxn];
int main() {
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int n;
        scanf("%d", &n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &a[i], &b[i]);
            for (int j = 0; j < i; ++j) {
                if ((a[i] - a[j]) * (b[i] - b[j]) < 0) {
                    ++ans;
                }
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

