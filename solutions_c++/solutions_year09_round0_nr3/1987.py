#include<stdio.h>
#include<algorithm>
char s1[29]=" welcome to code jam",s2[110];
int dp[120][120];
main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,t,i,j;
    gets(s2);
    T=atoi(s2);
    dp[0][0]=1;
    for(t=1;t<=T;t++){
        gets(s2+1);
        for(i=1;s2[i];i++){
            for(j=1;j<=19;j++){
                dp[i][j]=dp[i-1][j];
                if(s1[j]==s2[i])dp[i][j]+=dp[i-1][j-1];
                dp[i][j]%=10000;
            }
            dp[i][0]=1;
        }
        printf("Case #%d: %04d\n",t,dp[i-1][19]);
    }
}
