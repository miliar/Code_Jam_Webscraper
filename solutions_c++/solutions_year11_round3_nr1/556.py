#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

char tab[100][100];

int solve(int lz, int r, int c) {
  int res=0;

  int zost=0;
  REP(ir,r) {
    REP(ic, c) {
      if (ir<r-1 && ic<c-1 && tab[ir][ic]=='#' && tab[ir+1][ic]=='#' && tab[ir][ic+1]=='#' && tab[ir+1][ic+1]=='#')
        {
           tab[ir][ic]='/';
           tab[ir+1][ic]='\\';
           tab[ir][ic+1]='\\';
           tab[ir+1][ic+1]='/';
        }
      if (tab[ir][ic]=='#') zost++;
    }
  }


  printf("Case #%d:\n",lz+1);
  if (zost>0) {
    printf("Impossible\n");
  } else {
    REP(ir, r) {
      REP(ic, c) {
         printf("%c",tab[ir][ic]);
      }
      printf("\n");
    }  
  }
}


int main() {
  int t;
  scanf("%d", &t);

  REP(lz,t) {
    int r, c;
    scanf("%d %d\n", &r, &c);
    REP(ir, r) {
      REP(ic, c) {
         scanf("%c",&tab[ir][ic]);
      }
      scanf("\n");
    }
    solve(lz,r, c);
  }


}