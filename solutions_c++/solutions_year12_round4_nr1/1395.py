#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;


int T;

int D;

int n;

int l[10005],d[10005];

int dp[10005][10005];


int f(int x,int y){
    if (y!=-1){
       if (dp[x][y]!=-1) return dp[x][y];        
       }
    int L=min(l[x],d[x]-d[y]);   
    if (d[x]+L>=D) return 1;
    dp[x][y]=0;
    for (int i=x+1;i<n;i++){
        if (d[x]+L>=d[i]){
          dp[x][y]=max(dp[x][y],f(i,x));                
         } else break;
        }
    return dp[x][y];
    }




int main(){
    
    scanf("%d",&T);
    
    for (int t=1;t<=T;t++){
        scanf("%d",&n);
        for (int i=0;i<n;i++) scanf("%d %d",&d[i],&l[i]);
        scanf("%d",&D);
        bool B=false;
        memset(dp,-1,sizeof dp);
        
        if (f(0,-1)==1) B=true;
        
        if (B) printf("Case #%d: YES\n",t); else  printf("Case #%d: NO\n",t);
        
        }
    return 0;
    }
