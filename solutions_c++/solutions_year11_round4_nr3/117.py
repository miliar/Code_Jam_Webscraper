/**********************************************************************
Author: hanshuai
Created Time:  2011/6/4 23:48:33
File Name: c.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
const int maxn = 1000105;
bool p[maxn];
int main() {
    freopen("c.out", "w", stdout);
    int test, cas = 0;
    for(LL i = 2; i < maxn; i ++){
        if(p[i]) continue;
        for(LL j = i+i; j < maxn; j += i) p[j] = true;
    }
    LL N;
    scanf("%d", &test);
    while(test --){
        printf("Case #%d: ", ++cas);
        cin >> N;
        LL ans = 0;
        LL TM = (LL)sqrt((double)N) + 10;
        for(LL i = 2; i <= TM; i ++){
            if(p[i]) continue;
            LL x = i*i;
            while(x <= N){
                ans ++;
                x *= i;
            }
        }
        if(N != 1) ans ++;
        cout << ans << endl;
    }
    return 0;
}

