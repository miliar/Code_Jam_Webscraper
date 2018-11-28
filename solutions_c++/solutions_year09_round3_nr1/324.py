#include<cstdio>
#include<cstring>
char cmd[777];
int hash[777];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    scanf("%s",cmd);
    memset(hash,0,sizeof(hash));
    char*p=cmd;
    hash[*p]=2;
    int hashlen=1;
    while(*p){
      if(!hash[*p]){
        hash[*p]=hashlen++;
        if(hashlen==2)hashlen=3;
      }
      ++p;
    }
    --hashlen;
    if(hashlen<2)hashlen=2;
    __int64 sum=0;
    p=cmd;
    while(*p){
      sum=hashlen*sum+hash[*p]-1;
      ++p;
    }
    printf("Case #%d: %I64d\n",testi,sum);
  }
  return 0;
}