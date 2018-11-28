#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn=100002, maxk=17, inf = 1000000000;

int K,t,cas,n,d,ret,state;
int w[maxk][maxk],g[maxk][maxk][1<<maxk];
char s[maxn];

void init(){
  scanf("%d %s", &K, &s);
  n=strlen(s);
  d=n/K;
}

void solve(){
  memset(w, 0, sizeof(w));
  state = 1 << K;
  rep(i,K) rep(j,K) rep(a,state) g[i][j][a]= inf;
  rep(i, K) rep(j, K) rep(st, d) w[i][j] += s[st*K+i] != s[st*K+j];
  //printf("%d\n", g[0][0][0]);
  rep(a, state) rep(i, K) rep(j, K) {
    if(i==j|| (a&(1<<i)) || (a&(1<<j))) continue;
    if(a==0) {
      g[i][j][a] = w[i][j];
      continue;
    }
    rep(b, K) if (a & (1 << b)) 
      g[i][j][a] <?= g[i][b][a - (1 << b)] + w[b][j];
  }
}

int main(){
  scanf("%d",&cas);
  rep(tt, cas) {
    init();
    solve();
    ret = n;
    rep(i, K) rep(j, K) if (i != j) {
      int now = g[i][j][state - 1 - (1 << i) - (1 << j)];
      foru(st, 1, d - 1) now += s[st * K + i] != s[(st - 1) * K + j];
      ret <?= now;
    }
    printf("Case #%d: %d\n",tt+1, ret+1);
  }
  return 0;
}
