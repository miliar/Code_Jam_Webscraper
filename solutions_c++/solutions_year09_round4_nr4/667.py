/**********************************************************************
Author: hanshuai
Created Time:  2009-09-27 1:05:10
File Name: d.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const double eps = 1e-8;
typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;
struct T{
    int x, y, r;
    double tr;
}a[100];
int sgn(double v){
    return (v>eps)-(v<eps);
}
bool insert(int t1, int t2){
    return sgn(sqrt((a[t2].y-a[t1].y)*(a[t2].y-a[t1].y)
            +(a[t2].x-a[t1].x)*(a[t2].x-a[t1].x))-a[t1].tr-a[t2].tr) <= 0;
}
bool ins[100][100];
int n;
int vis[100];
bool dfs(int id, int v){
    if(vis[id] != -1 && vis[id] != v) return false;
    if(vis[id] == v) return true;
    vis[id] = v;
    for(int i = 0; i < n; i ++){
        if(!ins[id][i]) if(!dfs(i, v^1)) return false;
    }
    return true;
}
bool ok(double R){
    for(int i = 0; i < n; i ++){
        a[i].tr = R - a[i].r;
    }
    for(int i = 0; i < n; i ++){
        for(int j = 0; j < n; j ++){
            ins[i][j] = insert(i, j);
        }
    }
    memset(vis, -1, sizeof(vis));
    for(int i = 0; i < n; i ++){
        if(vis[i] == -1) if(!dfs(i, 0)) return false;
    }
    return true;
}
int main() {
    int test, cas = 0;
    freopen("d.out", "w", stdout);
    scanf("%d", &test);
    while(test --){
        scanf("%d", &n);
        for(int i = 0; i < n; i ++){
            scanf("%d%d%d", &a[i].x, &a[i].y, &a[i].r);
        }
        double low = 0.0, high = 1e10, mid, ans;
        while(sgn(low-high)<0){
            mid = (low + high)/2;
            if(ok(mid)){
                high = mid - eps;
//               printf("low = %.8lf high = %.8lf\n", low, high); 
                ans = mid;
            }else{
//                printf("low = %.8lf high = %.8lf\n", low, high);
                low = mid + eps;
            }
        }
        printf("Case #%d: %.7lf\n", ++cas, ans);
    }
    return 0;
}

