#include <iostream>
#include <cstring>

using namespace std;

char str[] = "welcome to code jam";
int ln;
char mas[512];
int dp[20][512];

int main()
{
    ln = strlen(str);
    int nt;
    int ls;
    scanf("%d\n",&nt);
    for(int i=1;i<=nt;i++)
    {
        memset(mas,0,sizeof(mas));
        fgets(mas,512,stdin);
        ls=strlen(mas);
        if(ls<ln)
        {
            printf("Case #%d: 0000\n",i);
            continue;
        }
        for(int j=0;j<ln;j++)
        {
            for(int k=0;k<ls;k++)
            {
                dp[j][k]= (k>0 ? dp[j][k-1] : 0) + ( mas[k]==str[j] ? (j==0 ? 1 : (k==0 ? 0 : dp[j-1][k-1])) : 0 );
                dp[j][k]%=10000;
            }
        }
        if(dp[ln-1][ls-1]==0) printf("Case #%d: 0000\n",i);
        else if(dp[ln-1][ls-1]< 10) printf("Case #%d: 000%d\n",i,dp[ln-1][ls-1]);
        else if(dp[ln-1][ls-1]< 100) printf("Case #%d: 00%d\n",i,dp[ln-1][ls-1]);
        else if(dp[ln-1][ls-1]< 1000) printf("Case #%d: 0%d\n",i,dp[ln-1][ls-1]);
        else printf("Case #%d: %d\n",i,dp[ln-1][ls-1]%10000);

    }
    return 0;
}
