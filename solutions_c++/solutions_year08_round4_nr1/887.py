#include <iostream>
#include <algorithm>
using namespace std;
#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ROF(i,n) for(int i=n-1;i>=0;--i)
const int INF = 1000000;

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum, ncases) {
    int n; scanf("%d",&n);
    int v; scanf("%d",&v);
    int g[n], c[n], val[n];
#define INT(i) (i<(n-1)/2)
    FOR(i,n) {
      if(INT(i)) {
        scanf("%d %d",&g[i],&c[i]);
      }
      else {
        scanf("%d", &val[i]);
      }
    }

    int gc[n][2], changes[n][2];
    FOR(i,n) {
      FOR(b,2) {
        if(not(INT(i))) gc[i][b] = INF;
        else if(g[i]==b) gc[i][b] = 0;
        else if(c[i]==1) gc[i][b] = 1;
        else gc[i][b] = INF;
      }
    }

#define LEFT(i) (2*(i)+1)
#define RIGHT(i) (2*(i)+2)
    ROF(i,n) {
      FOR(b,2)
        {
          if(INT(i)) {
            changes[i][b] = min(
                                gc[i][b] + changes[LEFT(i)][b] + changes[RIGHT(i)][b],
                                gc[i][1-b] + min(changes[LEFT(i)][b], changes[RIGHT(i)][b]));
            changes[i][b] = min(changes[i][b], INF);
          }
          else {
            changes[i][b] = (val[i]==b ? 0 : INF);
          }
        }
    }

    printf("Case #%d: ", casenum+1);
    if(changes[0][v]==INF) printf("IMPOSSIBLE\n");
    else printf("%d\n", changes[0][v]);
  }
  return 0;
}




