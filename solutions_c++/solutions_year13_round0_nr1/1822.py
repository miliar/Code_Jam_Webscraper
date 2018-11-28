// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

char a[10][10];

bool mam(char c, int x, int y, int dx, int dy) {
  if (0 <= x && x < 4)
    if (0 <= y && y < 4) 
      if(a[x][y]=='T' || a[x][y] ==c) return mam(c,x+dx,y+dy,dx,dy); else return false;
  return true;
}

void solve(){
  FOR(i,4) scanf("%s\n",a[i]);  
  vector<char> e;
  e.PB('X'); e.PB('O');
  FORSZ(q,e){
    bool uz=false;
    char c = e[q];
    FOR(i,4) if(mam(c,0,i,1,0)) uz=true;
    FOR(i,4) if(mam(c,i,0,0,1)) uz=true;
    if(mam(c,0,0,1,1)) uz=true;
    if(mam(c,3,0,-1,1)) uz=true;
    if(uz) { printf("%c won\n",c); return; }
  }
  bool uz=false;
  FOR(i,4) FOR(j,4) if(a[i][j]=='.') uz=true;
  if(uz) { printf("Game has not completed\n"); return; }
  printf("Draw\n");
}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
