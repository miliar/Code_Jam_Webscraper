#include <iostream>
#include <queue> 
#include <stdio.h>
#include <cstdlib>
#include <math.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string.h>
using namespace std; 
#define N 10000

char dp[N][N];
int d[N],l[N],D;
int n;
void init(){
    scanf("%d",&n);
    int i,j;
    for(i = 0; i < n; i++){
        scanf("%d%d",&d[i],&l[i]);
    }
    scanf("%d",&D);
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            dp[i][j] = 0;
}

char gao(int i,int j){
    if(dp[i][j] != 0) return dp[i][j];
    int x;
    if(j == 0) x = d[0];
    else x = min(l[j], d[j] - d[i]);
    if(d[j] + x >= D) return dp[i][j] = 1;
    for(int k = j+1; k < n; k++){
        if(d[k] - d[j] <= x){
            if(gao(j,k) == 1) return dp[i][j] = 1;
        }
        else break;
    }
    return dp[i][j] = 2;
}
int main()
{
//	freopen("in","r",stdin);
//	freopen("out","w",stdout);
    freopen("C:\\Users\\treert\\Downloads\\A-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\treert\\Downloads\\a.txt", "w", stdout);
    int T,cas = 0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++cas);
        init();
        if(gao(0,0) == 1) puts("YES");
        else puts("NO");
    }
      return 0;
}