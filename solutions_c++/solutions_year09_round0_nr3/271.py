#include<cstdio>
#include<cstring>
char a[555],*b="welcome to code jam";
int dp[22];
int main(){
  int test;
  scanf("%d",&test);
  gets(a);
  int testi;
  for(testi=1;testi<=test;++testi){
    memset(dp,0,sizeof(dp));
    gets(a);
    int i;
    for(i=0;a[i];++i){
      int j;
      for(j=0;b[j];++j)
        if(b[j]==a[i]){
          if(j)
            dp[j]=(dp[j]+dp[j-1])%10000;
          else *dp=(*dp+1)%10000;
        }
    }
    //for(i=0;b[i];++i)printf("%d ",dp[i]);
    printf("Case #%d: %04d\n",testi,dp[18]);
  }
  return 0;
}