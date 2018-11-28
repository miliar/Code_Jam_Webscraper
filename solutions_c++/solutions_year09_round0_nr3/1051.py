#include <iostream>
#include <string.h>
using namespace std;
#define MOD 10000

string wel="welcome to code jam";
int l=19;
char str[505];
int dp[505][20];
int len;
long long ans;

void solve()
{
        int i, j;
        for(i=0;i<len;i++)
        {
                for(j=0;j<l;j++)
                {
                        if(str[i]!=wel[j])      continue;
                        if(j==0)
                        {
                                dp[i][j]=1;
                                continue;
                        }
                        int temp=0;
                        for(int k=i-1;k>=0;k--)
                        {
                                if(str[k]==wel[j-1])
                                        temp=(temp+dp[k][j-1])%MOD;
                        }
                        dp[i][j]=temp;
                }
        }
}

int main()
{
        int T;
        int i,j;
        char t;
//        freopen("C-small-attempt1.in","r",stdin);
//        freopen("C-small-attempt1.out","w",stdout);

        freopen("C-large.in","r",stdin);
       freopen("C-large.out","w",stdout);
        cin>>T;
        getchar();
        for(int cases=1;cases<=T;cases++)
        {
                ans=0;
                memset(dp,0,sizeof(dp));
                gets(str);
                len=strlen(str);

                solve();

                for(i=0;i<len;i++)
                {
                        ans=(ans+dp[i][18])%MOD;
                }
                printf("Case #%d: %04d\n",cases,ans);
        }
        return 0;
}
