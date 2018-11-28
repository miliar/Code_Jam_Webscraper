#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

int ilosc[1000];

int solve(int lz, int x, int s, int r, int t, int n) {
  double czas=0;
  double zostr=t;

//      printf("---------\n");

  for(int pr=0; pr<=100; pr++) {
   int dr=ilosc[pr];
   if (dr>0) {
//      printf("* r=%d s=%d pr_r %f pr_s %f, droga=%d\n",r, s, pr*1.0+r, pr*1.0+s, dr);
      //pr - predkosc schodow
      if (zostr>0) {
        if (zostr*(pr+r)>=dr) {
          zostr = zostr - (dr*1.0/(pr+r));
          czas  = czas  + (dr*1.0/(pr+r));
        } else {
          double dr_r = zostr*(pr+r);
          double dr_s = dr - dr_r;
//          printf("%f %f\n", dr_r, dr_s);
          zostr = 0;
          czas = czas + (dr_r*1.0/(pr+r)) + (dr_s*1.0/(pr+s));
        }
      } else {
        czas = czas + (dr*1.0/(pr+s));
      }
//      printf("pr=%d dr=%d czas=%f\n",pr, dr, czas);
   }
  }
  printf("Case #%d: %0.9f\n",lz+1,czas);
}


int main() {
  int lt; //1-40
  scanf("%d", &lt);

  REP(lz,lt) {
    REP(i,1000) ilosc[i]=0;

    int x,s,r,t,n;
    scanf("%d %d %d %d %d\n", &x, &s, &r, &t, &n);

    int bez=x;
    REP(ir, n) {
     int b, e, w;
     scanf("%d %d %d\n",&b, &e, &w);
     ilosc[w]+=(e-b);
     bez=bez - (e-b);
    }
    ilosc[0]=bez;

    solve(lz, x, s, r, t, n);
  }


}