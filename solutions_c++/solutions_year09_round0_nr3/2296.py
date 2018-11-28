#include <cstdio>
#include <cstring>
const int MOD=10*1000;
int dp[100];
char w[] = "welcome to code jam";
char tmps[600];

int main()
{
  int LEN = strlen(w);
  int tt;
  scanf("%d\n",&tt);
  for(int t=1;t<=tt;t++) {
    int l=0;
    while(1) {
      char tmpc;
      scanf("%c", &tmpc);
      if(tmpc=='\n') break;
      tmps[l]=tmpc; 
      l++;
    }
    memset(dp,0,sizeof(dp));
    for(int i=0;i<l;i++)
      for(int j=0;j<LEN;j++)
	if(tmps[i]==w[j]) {
	  if(j==0) dp[0] = (dp[0]+1)%MOD;
	  else dp[j] = (dp[j]+dp[j-1])%MOD;
	}
    printf("Case #%d: ", t);
    if(dp[LEN-1]<10) printf("000");
    else if(dp[LEN-1]<100) printf("00");
    else if(dp[LEN-1]<1000) printf("0");
    printf("%d\n", dp[LEN-1]);	 
  }
}
