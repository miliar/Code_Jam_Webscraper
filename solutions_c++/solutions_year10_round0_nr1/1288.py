#include<cstdio>
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n,k;
    scanf("%d%d",&n,&k);
    printf("Case #%d: %s\n",testi,((k&(1<<n)-1)-(1<<n)+1)?"OFF":"ON");
  }
  return 0;
}