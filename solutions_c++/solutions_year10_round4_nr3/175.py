/**********************************************************************
Author: hanshuai
Created Time:  2010/6/5 23:40:23
File Name: c.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const int maxn = 105;
int a[maxn][maxn], b[maxn][maxn];
bool ok(int v[][maxn]){
    for(int i = 0; i < maxn; i ++){
        for(int j = 0; j < maxn; j ++){
//            printf("%d ", v[i][j]);
            if(v[i][j]) return false;
        }
//        printf("\n");
    }
    return true;
}
void cal(int t1[][maxn], int t2[][maxn]){
    for(int i = 0; i < maxn; i++){
        for(int j = 0; j < maxn; j ++){
            int x = i-1, y = j-1;
            if(x < 0 || y < 0) t2[i][j] = 0;
            else{
                t2[i][j] = t1[i][j];
                if(t2[i][j]){
                    if(!t1[i][y] && !t1[x][j]) t2[i][j] = 0;
                }else{
                    if(t1[i][y] && t1[x][j]) t2[i][j] = 1;
                }
            }
        }
    }
}
int main() {
    freopen("c.out", "w", stdout);
    int test, cas = 0;
    scanf("%d", &test);
    while(test --){
        int n, x1, y1, x2, y2;
        scanf("%d", &n);
        memset(a, 0, sizeof(a));
        for(int i = 0; i < n; i ++){
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for(int t1 = x1; t1 <= x2; t1 ++){
                for(int t2 = y1; t2 <= y2; t2 ++){
                    a[t1][t2] = 1;
                }
            }
        }
        int ans = 0;
        while(1){
            if(ok(a)) break;
            cal(a, b);
            ans ++;
            if(ok(b)) break;
            cal(b, a);
            ans ++;
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

