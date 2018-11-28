#include<cstdio>
#define M 100003
int c[555][555],dp[555][555],s[555];
void makec(){
  c[0][0]=1;
  int i;
  for(i=0;i<501;++i){
    c[i][0]=1;
    int j;
    for(j=1;j<=i;++j)
      c[i][j]=(c[i-1][j]+c[i-1][j-1])%M;
  }
}
int main(){
  makec();
  s[1]=s[2]=dp[1][1]=dp[2][1]=1;
  int i;
  for(i=3;i<501;++i){
    s[i]=1;
    dp[i][1]=1;
    int j;
    for(j=2;j<i;++j){
      dp[i][j]=0;
      int k;
      for(k=1;k<j;++k)
        if(i-j>=j-k)
          dp[i][j]=(dp[i][j]+(long long)dp[j][k]*c[i-j-1][j-k-1])%M;
      s[i]=(s[i]+dp[i][j])%M;
    }
  }
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n;
    scanf("%d",&n);
    printf("Case #%d: %d\n",testi,s[n]);
  }
  return 0;
}