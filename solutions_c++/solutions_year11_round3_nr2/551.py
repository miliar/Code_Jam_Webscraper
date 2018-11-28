#include <cstdio>
#include <cassert>
#include <vector>
#include <cstdlib>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

int tab[10000];

int solve(int lz, int l, int t , int n) {

  
  int minczas=0;
  REP(i,n) {
    minczas+=tab[i]*2;
  }

  if (l>=1) {
  REP(j,n) {
//    printf("speed w %d\n",j);
    int czas=0;
    int czas_got=t;
    // sym
    REP(i,n) {
      int czas_next=tab[i]*2;
      int czas_dod=czas_next;
      
      if (i==j) {
        if ( czas>=czas_got) {
          czas_dod = czas_next/2;
        } else if (czas+czas_next>czas_got) {
          int czas_norm = (czas_got-czas);
          int czas_fast = (czas+czas_next-czas_got)/2;
//          printf("** %d %d\n",czas_norm,czas_fast);
          czas_dod=czas_norm+czas_fast;
        }
      }
//      printf("  czas %d->%d %d\n",i,i+1,czas_dod);
      czas+=czas_dod;
    }
    if (czas<minczas) minczas=czas;
  }
  }

  if (l>=2) {
    REP(j1,n) {
      REP(j2,n) {
        if (j1!=j2) {
          int czas=0;
          int czas_got=t;
          REP(i,n) {
            int czas_next=tab[i]*2;
            int czas_dod=czas_next;
      
            if (i==j1 || i==j2) {
              if ( czas>=czas_got) {
                czas_dod = czas_next/2;
              } else if (czas+czas_next>czas_got) {
                int czas_norm = (czas_got-czas);
                int czas_fast = (czas+czas_next-czas_got)/2;
    //          printf("** %d %d\n",czas_norm,czas_fast);
               czas_dod=czas_norm+czas_fast;
              }
            }
            czas+=czas_dod;
          }
          if (czas<minczas) minczas=czas;
        }
      }
    }
  }
  

  /*
  printf("n=%d l=%d t=%d\n",n,l,t);
  REP(i,n) {
    printf("%d->%d droga=%d\n",i,i+1,tab[i]);
  }
  */
  
   
  printf("Case #%d: %d\n",lz+1, minczas);

}


int main() {
  int t;
  scanf("%d", &t);

  int tc[1000];
  REP(lz,t) {
    int l,t,n,c;
    scanf("%d %d %d %d", &l, &t, &n, &c);

    REP(i, c) {
      scanf("%d",&tc[i]);
    }
    REP(i,n) {
      tab[i]= tc[i %c ];
    }

    solve(lz, l, t, n);
  }


}