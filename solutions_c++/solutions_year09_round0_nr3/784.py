#include <stdio.h>
#include <string.h>
int main(){
    freopen("clarge.in","r",stdin);
    freopen("out.txt","w",stdout);
    char goal[]="welcome to code jam";
    char res[]="0000";
    char str[510];
    int dp[20][510];
    int T,t,l,i,j;
    scanf("%d ",&T);
    for (t=1;t<=T;t++){
        gets(str);
        l=strlen(str);
        memset(dp,0,sizeof(dp));
        if (str[0]==goal[0]) dp[0][0]=1;
        for (i=1;i<l;i++)
            if (str[i]==goal[0]) dp[0][i]=dp[0][i-1]+1;
            else dp[0][i]=dp[0][i-1];
        for (i=1;i<strlen(goal);i++)
            for (j=1;j<l;j++)
                if (str[j]==goal[i]) dp[i][j]=(dp[i-1][j-1]+dp[i][j-1])%10000;
                else dp[i][j]=dp[i][j-1]%10000;
        res[0]='0'+dp[strlen(goal)-1][l-1]/1000;
        dp[strlen(goal)-1][l-1]%=1000;
        res[1]='0'+dp[strlen(goal)-1][l-1]/100;
        dp[strlen(goal)-1][l-1]%=100;
        res[2]='0'+dp[strlen(goal)-1][l-1]/10;
        dp[strlen(goal)-1][l-1]%=10;
        res[3]='0'+dp[strlen(goal)-1][l-1];
        
        printf("Case #%d: %s\n",t,res);
    }
    return 0;
}
