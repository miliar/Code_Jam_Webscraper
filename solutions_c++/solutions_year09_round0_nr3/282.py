#include <stdio.h>
#include <string.h>

#define MAX 512

char str[MAX];

int dp[25][MAX];

char gcj[]="welcome to code jam";

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int tests;
  gets(str);
  sscanf(str,"%d",&tests);
  for(int test=1;test<=tests;++test) {
    gets(str);
    memset(dp,0,sizeof(dp));
    int l=strlen(gcj);
    int n=strlen(str);
    for(int i=0;i<=n;++i)
      dp[0][i]=1;
    for(int i=1;i<=l;++i) {
      for(int j=n-1;j>=0;--j) {
        dp[i][j]=dp[i][j+1];
        if(str[j]==gcj[l-i]) {
          dp[i][j]+=dp[i-1][j+1];
          if(dp[i][j]>=10000)
            dp[i][j]-=10000;
        }
      }
    }
    printf("Case #%d: %04d\n",test,dp[l][0]);
  }
  return 0;
}
