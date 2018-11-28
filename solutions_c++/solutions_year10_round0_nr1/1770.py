#include<cstdio>

int main(){
  int T, N, K;
  scanf("%d", &T);
  for(int i = 0; i < T; i++){
    scanf("%d%d", &N, &K);
    printf("Case #%d: ", i+1);
    
    K %= 1 << N;
    if(K == (1<<N) - 1){
      printf("ON\n");
    }else{
      printf("OFF\n");
    }
  }
  return 0;
}
