#include <iostream>
using namespace std;
char c[22]="welcome to code jam";
int dp[555][22];
char str[555];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,t,i,j;
    cin>>n;
    getchar();
    for(t=1;t<=n;t++)
    {
        str[0]='A';
        memset(dp,0,sizeof(dp));
        cin.getline(str+1,525);
        int len=strlen(str);
        for(i=1;i<=len-1;i++)
        {
            for(j=0;j<19;j++)
            {
                if(c[j]==str[i])
                {
                    if(j==0)
                    {
                        dp[i][0]=(dp[i-1][0]+1)%10000;
                    }
                    else
                    {
                        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10000;
                    }
                }
                else
                {
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        int ans=dp[len-1][18];
        printf("Case #%d: ",t);
            printf("%.4d\n",ans);

    }
    return 0;
}
