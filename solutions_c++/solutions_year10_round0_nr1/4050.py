#include<cstdio>

int main(){
  int N,K,T;
  scanf("%d",&T);
  for(int t=0;t<T;t++){
    scanf("%d %d",&N,&K);
    bool flag=true;
    for(int i=0;i<N;i++){
      bool tt=K%2;
      flag=flag and tt;
      K/=2;
    }
    printf("Case #%d: ",t+1);
    if(flag) printf("ON\n");
    else printf("OFF\n");
  }
}
