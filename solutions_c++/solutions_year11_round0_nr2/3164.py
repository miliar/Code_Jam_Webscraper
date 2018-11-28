#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

// BRUTE

int n;
char tab[10000];

int merge[32][32];
int usun[32][32];

int solve(int lz) {
  int dl=0;
  char wyn[10000];

  REP(i,n) {
    int c=tab[i]-64;
    int wstaw_c=1;
    if (dl>0) {
      int mer=merge[c][wyn[dl-1]-64];
      if (mer>0) {
        wyn[dl-1]=mer+64;
        wstaw_c=0;
      } else {
        REP(j,dl) {if (usun[wyn[j]-64][c]==1) {dl=0;wstaw_c=0;break;}}
      }
    }
    if (wstaw_c) {wyn[dl]=c+64; dl++;}
  }

  printf("Case #%d: [",(lz+1));
  REP(i,dl) {if (i>0) printf(", "); 
             printf("%c",wyn[i]);
            };
  printf("]\n");
}


int main() {
  int ilc;
  int t,i,lz,c;
  char c1,c2,c3;

  scanf("%d", &t);
  REP(lz,t) {
    REP(k1,32) REP(k2,32) {merge[k1][k2]=0; usun[k1][k2]=0;}

    scanf("%d", &c);
    REP(i,c) {
      scanf(" %c%c%c", &c1, &c2, &c3);
      merge[c1-64][c2-64]=c3-64;
      merge[c2-64][c1-64]=c3-64;
    }

    scanf("%d", &ilc);
    REP(i,ilc) {
      scanf(" %c%c", &c1, &c2, &c3);
      usun[c1-64][c2-64]=1;
      usun[c2-64][c1-64]=1;
    };

    scanf("%d ", &n);
    REP(i,n) scanf("%c", &tab[i]);

    solve(lz);
  }


}