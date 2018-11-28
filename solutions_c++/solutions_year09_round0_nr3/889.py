#include <iostream>
#include <cstring>
using namespace std;
int dp[510][20],s,t,i,j,sum,l;
char w[510];
char str[20]="welcome to code jam";
int main(){
    freopen("C-large.in", "r", stdin);
    freopen("out32.txt", "w", stdout);
    s=1;
    scanf("%d",&t);
    gets(w);
    while(t>0)
    {
        t--;
        gets(w);
        l=strlen(w);
        memset(dp, 0, sizeof(dp));
        sum=0;
        for(i=0;i<l;++i)
        {
            if(w[i]=='w') dp[i][0]=++sum;
            else dp[i][0]=sum;
        }
        for(i=1;i<l;++i)
        {
            for(j=1;j<19;++j)
            {
            if(w[i]==str[j]) dp[i][j] =dp[i-1][j]+dp[i-1][j-1];
                else dp[i][j]=dp[i-1][j];
            dp[i][j]%=10000;
            }
        }
        printf("Case #%d: %04d\n",s++,dp[l-1][18]);
    }
    return 0;
}
