/*
 * Author: OpenLegend
 * Created Time:  2011-5-7 15:53:55
 * File Name: dt.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    freopen("d.out", "w", stdout);
    int test, n, tmp, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d", &n);
        int ans = n;
        for(int i = 1; i <= n; i ++){
            scanf("%d", &tmp);
            if(i == tmp) ans --;
        }
        printf("Case #%d: %.9lf\n", ++cas, (double)ans);
    }
    return 0;
}

