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

int m, n;
char str[100][100];

int dp[10][1<<10];

bool valid(int s, int r) {
  int i;
  for(i=0;i<n;i++)
    if( str[r][i] == 'x' && ( s & (1<<i) ) )
      return false;
  re true;
}

bool xyz(int s) {  // side by side
 int i;
 for(i=1;i<n;i++)
   if( (s & (1<<i) ) && (s & (1<<(i-1))) ) re false;
 re true;

}

bool upore(int u, int d) {
     int i;
  for(i=1;i<n;i++) {
    if( ( d & (1<<i) ) && (u & (1<<(i-1))) ) re false;
  }
  for(i=0;i+1<n;i++) {
    if( ( d & (1<<i) ) && (u & (1<<(i+1))) ) re false;
  }
  re true;
}

int count(int s) {
    int i;
    int c = 0;
    for(i=0;i<n;i++)
      if( s & (1<<i) ) c++;
    re c;
}

int memo(int r, int s) {
  if( r == m ) re 0;
  if( dp[r][s] != -1 ) re dp[r][s];
 
  int res = 0;
  int i;
  for(i=0;i<(1<<n);i++) {
    if( xyz(i) && valid(i, r) && upore(s, i) ) {
      int k = count(i) + memo(r+1, i);
      res >?= k;
    }
  }
  re dp[r][s] = res;
}

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t;
    int cases = 1;
    for( sf("%d", &t); t--;  ) {
      sf("%d %d", &m, &n);
      int i, j;
      for(i=0;i<m;i++)
        sf("%s", str[i]);
      for(i=0;i<m;i++)
        for(j=0;j < (1<<n); j++)
          dp[i][j] = -1;
      
      int res = memo(0, 0);
      pf("Case #%d: %d\n", cases++, res);
    }
    return 0;
}
