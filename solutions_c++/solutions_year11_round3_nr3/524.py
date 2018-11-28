#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

int tab[10000];

int solve(int lz, int n, int l, int h) {
  printf("Case #%d: ",lz+1);

  int res=0;

/*REP(i,n) {
  printf("%d\n",tab[i]);
}
*/

  for (int li=l; li<=h; li++) {
    int dziel=0;
    REP(j,n) {
      if (tab[j]%li==0 || li%tab[j]==0) {dziel++;}
      else {
        break;
      }
    }
    if (dziel==n) {
      printf("%d\n",li); return 0;
    }
  }

  printf("NO\n");
}


int main() {
  int t;
  scanf("%d", &t);

  REP(lz,t) {
    int n,l,h;
    scanf("%d %d %d", &n, &l, &h);

//    printf("%d %d %d\n", n, l, h);
    REP(i, n) {
      scanf("%d",&tab[i]);
    }
    solve(lz, n, l, h);
  }


}