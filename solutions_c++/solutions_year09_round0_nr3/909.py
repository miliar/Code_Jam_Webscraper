#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

int res,dp[20];
string s,a="welcome to code jam";

int main()
{
    freopen("d://in.txt","r",stdin);
    freopen("d://out.txt","w",stdout);
    int T,i,j,len,cas=1;
    scanf("%d",&T);
    getchar();
    while (T--)
    {
        getline(cin,s);
        memset(dp,0,sizeof(dp));
        res=0;
        len=s.length();
        for (i=0;i<len;i++)
        {
            for (j=18;j>=0;j--)
            {
                if (s[i]==a[j])
                {
                    if (j==0)
                    {
                        dp[j]++;
                    }
                    else
                    {
                        dp[j]=(dp[j]%10000+dp[j-1]%10000)%10000;
                    }
                }
            }
        }
        printf("Case #%d: %04d\n",cas++,dp[18]%10000);
    }
    //system("pause");
    return 0;
}
