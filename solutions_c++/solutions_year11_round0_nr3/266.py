/*
 * Author: OpenLegend
 * Created Time:  2011-5-7 15:12:02
 * File Name: c.cpp
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
    freopen("c.out", "w", stdout);
    int test, n, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d", &n);
        int sum = 0, s2 = 0, tmp, tm = 1234567890;
        for(int i = 0; i < n; i ++){
            scanf("%d", &tmp);
            tm = min(tm, tmp);
            sum += tmp;
            s2 ^= tmp;
        }
        printf("Case #%d: ", ++cas);
        if(s2 != 0) printf("NO\n");
        else{
            printf("%d\n", sum-tm);
        }
    }
    return 0;
}

