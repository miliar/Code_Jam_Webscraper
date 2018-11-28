#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

int n;
char tabc[1000];
int  tabn[1000];

struct elem {
  int pos;
};

int solve(int lz) {
  int res=0;
  elem O, B;

  O.pos=1;
  B.pos=1;

  REP(i,n) {
    int nextO=0;
    int nextB=0;
    for (int j=i; j<n; j++) if (tabc[j]=='O') {nextO=tabn[j]; break;}
    for (int j=i; j<n; j++) if (tabc[j]=='B') {nextB=tabn[j]; break;}

//    printf("---------\n");
//    printf("%d %d %d\n",i, nextO, nextB);

    if (tabc[i]=='O' && nextO>0) { //kolej na O
      int ruch=abs(nextO-O.pos)+1;
//      printf("O ruch o %d z %d do %d\n",ruch, O.pos, nextO);
      res+=ruch;
      O.pos=nextO;

      if (nextB>0) {
        if (abs(nextB-B.pos)<=ruch) {
          B.pos=nextB;
//          printf("B ruch przesuwam do %d\n",nextB);
        } else {
//          printf("B ruch z %d do ",B.pos);
          if (B.pos<nextB) B.pos+=ruch; else B.pos-=ruch;
//          printf("%d\n",B.pos);
        }
      }
    }



    if (tabc[i]=='B' && nextB>0) { //kolej na B
      int ruch=abs(nextB-B.pos)+1;
//      printf("B ruch o %d z %d do %d\n",ruch, B.pos, nextB);
      res+=ruch;
      B.pos=nextB;

      if (nextO>0) {
        if (abs(nextO-O.pos)<=ruch) {
          O.pos=nextO;
//          printf("O ruch przesuwam do %d\n",nextO);
        } else {
//          printf("O ruch z %d do ",O.pos);
          if (O.pos<nextO) O.pos+=ruch; else O.pos-=ruch;
//          printf("%d\n",O.pos);
        }
      }
    }

  }

  printf("Case #%d: %d\n",lz+1,res);
}


int main() {
  int t,i,lz;

  scanf("%d", &t);
//  t=3;
  REP(lz,t) {
    scanf("%d", &n);
    REP(i,n) {
      scanf(" %c %d", &tabc[i], &tabn[i]);
//      printf("%c|%d|\n", tabc[i], tabn[i]);
    }
    solve(lz);
  }


}