#define MAX 100
#include <cstdio>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)


int frequencies[MAX];


int main(){
  int T,t,N,L,H,i,freq;
  scanf("%d\n",&T);
  REP(t,T){
    scanf("%d %d %d\n",&N,&L,&H);
    REP(i,N){
      scanf("%d ",&frequencies[i]);
    }
    scanf("\n");
    bool possible = false;
    for (int i=L; i<=H; i++){
      // this frequency works?
      bool b = true;
      for (int j=0; j<N; j++){
        if (!((frequencies[j] % i == 0) or (i % frequencies[j] == 0))) b = false;
      }
      if ((b == true) && !possible){
        possible = true;
        freq = i;
      }
    }
    if (possible) printf("Case #%d: %d\n",t+1,freq); else printf("Case #%d: NO\n",t+1);
  }
  return 0;
}
 
