/*
 * Author: OpenLegend
 * Created Time:  2011-5-7 12:32:51
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
char buf[10];
int main() {
    freopen("a.out", "w", stdout);
    int test, cas = 0, n;
    scanf("%d", &test);
    while(test --){
        scanf("%d", &n);
        int p0 = 1, p1 = 1, t0 = 0, t1 = 0;
        for(int i = 0; i < n; i ++){
            int loc;
            scanf("%s%d", buf, &loc);
            int cur = max(t0, t1);
            if(buf[0] == 'O'){
                t0 = max(cur, abs(p0-loc)+t0) + 1;
                p0 = loc;
            }else{
                t1 = max(cur, abs(p1-loc)+t1) + 1;
                p1 = loc;
            }
        }
        printf("Case #%d: %d\n", ++cas, max(t0, t1));
    }
    return 0;
}

