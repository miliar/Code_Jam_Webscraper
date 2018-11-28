#include<iostream>
#include<string>
using namespace std;
int dp[505][20];
char st[505];
string s="welcome to code jam";
int main()
{
    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );
    int i,j,l;
    int t,T;
    scanf("%d",&T);
    getchar();
    for(t=1;t<=T;t++)
    {
        gets(st);
        l=strlen(st);
        memset(dp,0,sizeof(dp));
        for(i=1;i<=l;i++)
        {
            if(st[i-1]=='w')
                dp[i][1]=(dp[i-1][1]+1)%10000;
            else
                dp[i][1]=dp[i-1][1]%10000;
        }
        for(i=2;i<20;i++)
            for(j=2;j<=l;j++)
            {
                if(st[j-1]==s[i-1])
                    dp[j][i]=(dp[j-1][i]+dp[j-1][i-1])%10000;
                else
                    dp[j][i]=(dp[j-1][i])%10000;
             }
        printf("Case #%d: %04d\n",t,dp[l][19]%10000);
    }
    return 0;
}
