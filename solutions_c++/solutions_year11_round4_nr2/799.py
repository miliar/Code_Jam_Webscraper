#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define EPS (1e-8)
#define EQ(a,b) (a-b>-EPS && a-b<EPS)

char buf[1024];

int main() {
  int T, tc = 0; scanf("%d", &T);
  
  while(T--) {
    int w, h, d; scanf("%d%d%d", &h, &w, &d);
    vector<string> m(h);
    rep(i, h) { scanf("%s", buf); m[i] = buf; }
    
    int res = -1;
    
    for(int k=min(w, h); k>=3 && res==-1; k--) {
      for(int x=0; x+k<=w && res==-1; x++) {
        for(int y=0; y+k<=h && res==-1; y++) {
          
          double tx = 0.0, ty = 0.0;
          for(int xx=x; xx<x+k; xx++) {
            for(int yy=y; yy<y+k; yy++) {
              if(xx==x && yy==y) continue;
              if(xx==x && yy==y+k-1) continue;
              if(xx==x+k-1 && yy==y) continue;
              if(xx==x+k-1 && yy==y+k-1) continue;
              tx += (xx-x-k/2.0+0.5) * (m[yy][xx]-'0'+d);
              ty += (yy-y-k/2.0+0.5) * (m[yy][xx]-'0'+d);
            }
          }
          if(EQ(tx, 0.0) && EQ(ty, 0.0)) res = k;
          
        }
      }
    }
    
    if(res == -1)
      printf("Case #%d: IMPOSSIBLE\n", ++tc);
    else
      printf("Case #%d: %d\n", ++tc, res);
  }
  
  return 0;
}
