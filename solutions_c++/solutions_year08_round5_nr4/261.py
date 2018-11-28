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

int grid[101][101],  dp[101][101];
int h, w;
int res;
int mod = 10007;

bool valid(int r, int c) {
     return r >= 1 && r <= h && c >= 1 && c <= w;
}

int memo(int r, int c) {
  if( r == h && c == w ) re 1;
  if( dp[r][c] != -1 ) re dp[r][c];
  int rr = r + 1;
  int cc = c + 2;
  int res = 0;
  if( valid(rr, cc) && grid[rr][cc] == 0 ) {
    res += memo(rr, cc);
    res %= mod;
  }
  
  rr = r + 2;
  cc = c + 1;
  if( valid(rr, cc) && grid[rr][cc] == 0 ) {
    res += memo(rr, cc);
    res %= mod;
  }
  
  re dp[r][c] = res;
  
}

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int t;
    int cases = 1;
    for( sf("%d", &t); t--;  ) {
      sf("%d %d %d", &h, &w, &res);
      int i, j;
      for(i=1;i<=h;i++) 
        for(j=1;j<=w;j++)
          grid[i][j] = 0, dp[i][j] = -1;;
      while(res--) {
        int r, c;
        sf("%d %d", &r, &c);
        grid[r][c] = 1;
      }
      
      int res = memo(1, 1);
      printf("Case #%d: %d\n", cases++, res);
      
    }
    return 0;
}
