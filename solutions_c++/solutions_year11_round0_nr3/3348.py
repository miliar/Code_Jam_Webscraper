#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

#define REP(i,n) for (int _n=n, i=0; i<_n; ++i)
typedef long long LL;

int n;
int tab[10000];

int lz;

int solve(int lz) {

  int m=1<<n;
  
//  printf("%d\n",m);
  int maxx=-1;
  for (int i=1; i<m-1; i++) {
    int b=i;
    int kupka1=0;
    int kupka2=0;
    int xor1=0;
    int xor2=0;
    REP(j,n) {
      if ((b&1)==0) {kupka1+=tab[j]; xor1=xor1^tab[j];}
               else {kupka2+=tab[j]; xor2=xor2^tab[j];}
      b=b/2;
    }
    if (xor1==xor2) {if (kupka1>maxx) maxx=kupka1;}
//      printf("%d %d %d %d \n",kupka1, kupka2, xor1, xor2);
    
  }

    if (maxx==-1) {
      printf("Case #%d: NO\n",lz+1);
    } else {
      printf("Case #%d: %d\n",lz+1,maxx);
    }

}

int main() {
  int t,i;

  scanf("%d", &t);
  REP(lz,t) {
    scanf("%d", &n);
    REP(i,n) {
      scanf("%d", &tab[i]);
    }
    solve(lz);
  }


}