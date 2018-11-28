/**********************************************************************
Author: hanshuai
Created Time:  2010/5/8 19:54:34
File Name: c.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long LL;
const int maxn = 1005;
LL g[maxn], v[maxn];
int next[maxn];
int main() {
    freopen("c.out", "w", stdout);
    int test, cas = 0;
    LL r, k, n;
    scanf("%d", &test);
    while(test --){
        scanf("%I64d%I64d%I64d", &r, &k, &n);
        for(int i = 0; i < n; i ++){
            scanf("%I64d", &g[i]);
        }
        memset(next, -1, sizeof(next));
        for(int i = 0; i < n; i ++){
            if(g[i] > k) continue;
            v[i] = g[i];
            for(int j = (i+1)%n; ; j = (j+1)%n){
                if(i == j || v[i]+g[j] > k){
                    next[i] = j; break;
                }
                v[i] += g[j];
            }
        }
        int th = 0;
        LL ans = 0;
        for(int i = 0; i < r; i ++){
            if(next[th] == -1) break;
            ans += v[th];
            th = next[th];
        }
        printf("Case #%d: ", ++cas);
        printf("%I64d\n", ans);
    }
    return 0;
}

