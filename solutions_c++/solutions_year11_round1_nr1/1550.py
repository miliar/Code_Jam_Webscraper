#include <cstdio>
using namespace std;
int N,D,G,Q,T,K,A,B,G1,G0,K1,K0,bedone;
int main(){
  scanf("%d",&Q);
  for(int q=1;q<=Q;q++){
      scanf("%d %d %d",&N,&D,&G);
      T=100-D;
      K=100-G;
      bedone=0;
      for(int i=1;i<=N;i++){
          A=D*i; //%100==0
          B=T*i; //%100==0
          G0=100-((i*G)%100);
          K0=100-((i*K)%100);
          G1=A-(i+G0)*G;
          K1=B-(i+K0)*K;
          //printf("%d %d %d|%d %d %d %d\n",i,D,G,A,B,G1,K1);
          if ((A%100==0) && (B%100==0) && (G1<=0) && (K1<=0))
              bedone=1;
      }
      if(bedone==1)
        printf("Case #%d: Possible\n",q);
      else
        printf("Case #%d: Broken\n",q);
  }
}
