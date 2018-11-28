#include<cstdio>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
#include<sstream>

using namespace std;

#define pf printf
#define sf scanf
#define co continue
#define re return
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

int inf = 100000000;

int A[10100];
int g[10100];
int c[10100];
int val[10100];
int m, v;
int leaf;
int dp[10100][2];

int memo(int u, int v) {
  
  if( u >= leaf ) {
    if( v == val[u] ) return 0;
    else return inf;
  }  
  
  if( dp[u][v] != -1 ) re dp[u][v];
  // leave as it is..  
    int res = inf;
    if( v == 1 ) {
      if( g[u] == 1 ) {
        int k = memo(u*2, 1) + memo(u*2+1, 1); 
        res <?= k;
      }
      if( g[u] == 0 ) {
        int k = memo(u*2, 1);
        res <?= k;
        k = memo(u*2 + 1, 1);
        res <?= k;
      }
    }
    else {
      if( g[u] == 1 ) {
        int k = memo(u*2, 0);
        res <?= k;
        k = memo(u*2 + 1, 0);
        res <?= k;
      }
      if( g[u] == 0 ) {
        int k = memo(u*2, 0) + memo(u*2+1, 0);
        res <?= k;
      }
    }
    
    //change
    
    if( c[u] == 1 ) {
       if( v == 1 ) {
         if( g[u] == 1 ) {
           // make to orage
           int k = 1 + memo(u*2, 1);
           res <?= k;
           k = 1 + memo(u*2 + 1, 1);
           res <?= k;
         }
         else {
           //make and
           int k = 1 + memo(u*2, 1) + memo(u*2+1, 1); 
           res <?= k;
         }
       }
       
       else { // v = 0
          if( g[u] == 1 ) {
            int k = 1 + memo(u*2, 0) + memo(u*2+1, 0);
            res <?= k;
          }
          else {
            int k = 1 + memo(u*2, 0);
            res <?= k;
            k = 1  +memo(u*2 + 1, 0);
            res <?= k;
          }
       }
    }
    
    re dp[u][v] = res;
  
}

int main() {
    freopen("abig.in","r",stdin);
    freopen("abig.out","w",stdout);
    int t;
    int cases=1;
    for( sf("%d", &t); t--;  ) {
      sf("%d %d", &m, &v);
      int i, j;
      for(i=1;i<=(m-1)/2;i++) {
          sf("%d", &g[i]);
          sf("%d", &c[i]);
      } 
      for(i=1;i<=m;i++) val[i] = -1;
      leaf = (m-1)/2+1;
      int tot = (m+1)/2;
      for(i=(m-1)/2+1; tot--; i++)
        sf("%d", &val[i]);    
       
      for(i=1;i<=m;i++)
        for(j=0;j<2;j++)
          dp[i][j] = -1;
      int res = memo(1, v); 
      
      if( res >= inf - 10 ) {
        pf("Case #%d: IMPOSSIBLE\n", cases++);
      }
      else
        pf("Case #%d: %d\n", cases++, res);
      
    }
    return 0;
}

