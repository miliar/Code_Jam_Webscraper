/*
 * Author: xay
 * Created Time:  2010-5-23 18:19:31
 * File Name: b.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;

int main() {
    freopen("b.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int l, p, c;
        scanf("%d%d%d", &l, &p, &c);
        int cnt = 0;
        for (long long i = l; i < p; i *= c) {
            ++cnt;
        }
        int ans = 0;
        while (cnt > 1) {
            cnt = cnt - cnt / 2;
            ++ans;
        }
        printf("%d\n", ans);
    }
    return 0;
}

