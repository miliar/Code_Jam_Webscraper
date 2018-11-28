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

int cal(int x1, int y1, int x2, int y2, int x3, int y3) {
  return x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1 - y2);
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    int cases = 1;
    int i;
    for( sf("%d", &t); t--;  ) {
      int n, m, a;
      sf("%d %d %d", &n, &m, &a);
      int x1, x2, x3, y1, y2, y3;
      int xx1, xx2, xx3, yy1, yy2, yy3;
      xx1 = -1;
      for(x2=0;xx1 == -1 && x2<=n;x2++)
        for(y2=0;y2<=m && xx1 == -1;y2++)
          for(x3=0;x3<=n;x3++)
            for(y3=0;y3<=m;y3++) {
              int ar = cal(0,0,x2,y2,x3,y3);
              if( ar == a ) {
                xx1 = 0, xx2 = x2, xx3 = x3, yy1 = 0, yy2 = y2, yy3 = y3;
              }
            }
      if( xx1 == -1 ) {
        pf("Case #%d: IMPOSSIBLE\n", cases++);
      }
      else {
        pf("Case #%d: %d %d %d %d %d %d\n", cases++, xx1, yy1, xx2, yy2, xx3, yy3);
      }
    }
    return 0;
}

