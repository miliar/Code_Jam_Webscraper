#include<cstdio>
int main(){
  int t,tt,n,k;
  scanf("%d",&t);
  for(tt=1;tt<=t;tt++){
    scanf("%d",&n);
    scanf("%d",&k);
    printf("Case #%d: ",tt);
    if((k+1)%(1<<n)){
      printf("OFF\n");
    }else{
      printf("ON\n");
    }
  }
}
