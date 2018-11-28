/* 
 * File:   main.cpp
 * Author: Prowindy
 *
 * Created on 2011年5月7日, 下午12:33
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
int n, arr[1010];

/*
 * 
 */
int main(int argc, char** argv) {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int i, j, k;
    int t, cas;
    int sum, cur;
    int m, ans;
    scanf("%d", &t);
    for (cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        sum = 0;
        m = 0;
        for (i = 1; i <= n; i++) {
            scanf("%d", &arr[i]);
            sum ^= arr[i];
            m = max(m, arr[i]);
        }
        printf("Case #%d: ", cas);
        if (sum != 0) {
            printf("NO\n");
            continue;
        }
        sort(arr + 1, arr + n + 1);
        sum = 0;
        for (i = 2; i <= n; i++) {
            sum += arr[i];
        }
        printf("%d\n", sum);
    }
    return 0;
    return (EXIT_SUCCESS);
}

