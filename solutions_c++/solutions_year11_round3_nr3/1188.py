/*
 * File:   main.cpp
 * Author: Young
 *
 * Created on 2011年5月22日, 下午6:03
 */

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define PI acos(-1.0)
using namespace std;
#define M 100000
long long a[10000];
long long n, l, h;
int ans;

bool q() {
    for (int i = l; i <= h; i++) {
        int t = 0;
        for (int j = 0; j < n; j++) {
            if (i % a[j] == 0 || a[j] % i == 0)t++;
        }
        if (t == n) {
            ans = i;
            return true;
        }
    }
    return false;
}

int main(int argc, char** argv) {
    int cas;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &cas);
    for (int th = 1; th <= cas; th++) {
        cin >> n >> l >> h;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        printf("Case #%d: ", th);
        if (q())printf("%d\n", ans);
        else printf("NO\n");
    }
    return 0;
}

