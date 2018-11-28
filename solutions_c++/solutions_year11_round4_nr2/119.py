/**********************************************************************
Author: hanshuai
Created Time:  2011/6/4 22:09:03
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
const int maxn = 505;
typedef long long LL;
typedef pair<LL,LL> PLL;
int R, C;
char buf[maxn];
int g[maxn][maxn];
pair<LL,LL> p[2][maxn][maxn], sum[2][maxn][maxn];
void add(PLL& x, PLL v, int v2){
    x.first += v.first*v2;
    x.second += v.second*v2;
}
pair<LL,LL> cal(int id, int x0, int x1, int y0, int y1){
    pair<LL,LL> ret = sum[id][x1][y1];
    if(x0-1 >= 0) add(ret, sum[id][x0-1][y1], -1);
    if(y0-1 >= 0) add(ret, sum[id][x1][y0-1], -1);
    if(x0-1 >= 0 && y0-1 >= 0) add(ret, sum[id][x0-1][y0-1], 1);
//    cout << ret.first << " " << ret.second << endl;
    add(ret, p[id][x0][y0], -1);
    add(ret, p[id][x0][y1], -1);
    add(ret, p[id][x1][y0], -1);
    add(ret, p[id][x1][y1], -1);
    return ret;
}
bool ok(int x0, int x1, int y0, int y1){
    pair<LL,LL> l0 = cal(0, x0, x1, y0, y1);
    pair<LL,LL> l1 = cal(1, x0, x1, y0, y1);
    LL lx = x0+x1, ly = y0+y1;
//    cout << l0.first << " " << l0.second << " " << l1.first << " " << l1.second << endl;
//    cout << lx << " " << ly << endl;
    return (l0.first-l1.first*lx) == 0 && (l0.second-l1.second*ly) == 0;
}
int main() {
    freopen("b2.out", "w", stdout);
    int test, D, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d%d%d", &R, &C, &D);
        for(int i = 0; i < R; i ++){
            scanf("%s", buf);
            for(int j = 0; j < C; j ++){
                g[i][j] = buf[j] - '0';
            }
        }
        for(int i = 0; i < R; i ++){
            for(int j = 0; j < C; j ++){
                p[0][i][j] = make_pair(2*i*g[i][j], 2*j*g[i][j]);
                p[1][i][j] = make_pair(g[i][j], g[i][j]);
                for(int k = 0; k < 2; k ++){
                    sum[k][i][j] = p[k][i][j];
                    if(i-1 >= 0) add(sum[k][i][j], sum[k][i-1][j], 1);
                    if(j-1 >= 0) add(sum[k][i][j], sum[k][i][j-1], 1);
                    if(i-1 >= 0 && j-1 >= 0) add(sum[k][i][j], sum[k][i-1][j-1], -1);
                }
            }
        }
        int ans = 2;
        for(int i = 0; i < R; i ++){
            for(int j = 0; j < C; j ++){
                for(int k = ans+1; ; k ++){
                    if(i + k-1 >= R || j + k-1 >= C) break;
                    if(ok(i, i+k-1, j, j+k-1)){
                        ans = max(ans, k);
//                        printf("%d %d %d\n", i, j, k);
                    }
                }
            }
        }
//        printf("%d\n", ans);
        printf("Case #%d: ", ++cas);
        if(ans == 2) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}


