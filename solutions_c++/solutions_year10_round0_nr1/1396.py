#include<cstdio>
#include<cstring>
int main(){
  
  int T;
  long long N,K;
  long long prendidos;
  scanf("%d",&T);
  for (int k=1; k <= T; ++k){
    scanf("%lld %lld",&N,&K);
    printf("Case #%d: ",k);
    prendidos = 1 << N;
    K = K%prendidos;
    if (K == (prendidos - 1)) printf("ON\n");
    else printf("OFF\n");
  }
  return 0;
}