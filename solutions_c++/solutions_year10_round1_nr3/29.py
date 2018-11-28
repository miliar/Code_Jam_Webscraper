/**********************************************************************
Author: hanshuai
Created Time:  2010/5/22 10:18:59
File Name: c2.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
typedef long long LL;
const int maxn = 10000005;
int X[maxn], cur;
bool ok(int a, int b){
    if(a > b) swap(a, b);
    if(b < cur) return a <= X[b];
    if(a == 0) return true;
    if(b >= 2*a) return true;
    return !ok(b-a, a);
}
int main() {
    freopen("c2.out", "w", stdout);
    int test, A1, A2, B1, B2;
    int cas = 0;
    for(int i = 1; i < maxn; i ++){
        cur = i;
        int l = 0, r = i, mid; 
        while(l <= r){
            mid = (l+r)>>1;
            if(ok(mid, i)){
                X[i] = mid;
                l = mid + 1;
            }else r = mid - 1;
        }
    }
    
    scanf("%d", &test);
    while(test --){
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        LL ans = 0;
        for(int i = A1; i <= A2; i ++){
            int l = max(1, B1), r = min(X[i], B2);
            ans += max(0, (r-l+1));
        }
        for(int i = B1; i <= B2; i ++){
            int l = max(1, A1), r = min(X[i], A2);
            ans += max(0, (r-l+1));
        }
        printf("Case #%d: %I64d\n", ++cas, ans);
    }
    return 0;
}

