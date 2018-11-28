/* 
 * File:   gcjqr_C.cpp
 * Author: xhSong
 * Created on 2010年5月8日, 上午9:26
 * Time Complexity :
 * Space Complexity : 
 * Describe : 
 */

#include <cstdio>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <iterator>
#include <algorithm>
#define M 1001

using namespace std;

int a[M], next[M], s[M], v[M], ans[M];

int main(int argc, char** argv) {
    freopen("C-large", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, r, k, n;
    scanf("%d", &T);
    for(int test = 1; test <= T; test ++) {
        scanf("%d%d%d", &r, &k, &n);
        for(int i = 0; i < n; i ++) {
            scanf("%d", a + i);
        }
        printf("Case #%d: ", test);
        if(n == 1) {
            if(a[0] <= k) {
                printf("%lld\n", (long long)a[0] * r);
            }
            else {
                puts("0");
            }
            continue;
        }
        for(int i = 0; i < n; i ++) {
            int j = i, tmp = 0;
            while(j < i + n && tmp + a[j % n] <= k) {
                tmp += a[(j++) % n];
            }
            next[i] = j % n, s[i] = tmp;
        }
        long long sum = 0;
        memset(v, 0, sizeof(v));
        int i, p = 0;
        for(i = 1; i <= r; i ++) {
            if(v[p]) {
                break;
            }
            v[p] = i;
            sum += s[p];
            ans[i] = s[p];
            p = next[p];
        }
        if(i <= r && i - v[p] > 0) {
            long long tmp = 0;
            for(int j = v[p]; j < i; j ++) {
                tmp += ans[j];
            }
            sum += (r - i + 1) / (i - v[p]) * tmp;
            for(int j = 0; j < (r - i + 1) % (i - v[p]); j ++) {
                sum += ans[j + v[p]];
            }
        }
        printf("%lld\n", sum);
    }
    return 0;
}

