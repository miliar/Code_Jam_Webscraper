#include<iostream>

using namespace std;
#define size(x) (int)((x).size())
#define For(i,x) for(int i=0;i<x;i++)
#define Forn(i,y,x) for(int i=y;i<=x;i++)
#define Fill(a, v) memset(a, v, sizeof(a))

int main()
{
    #ifdef FAMEOFLIGHT_HOME
        freopen("C-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int N ,l1=19,l2;
    char str2[505];
    string str1="welcome to code jam";
    int dp[505][25];
    Fill(dp,0);
    scanf("%d\n",&N);
    Forn(kase,1,N)
    {
            gets(str2);
            Fill(dp,0);
            l2 = strlen(str2);
            For(i,l2)
            {
                    For(j,l1)
                    {
                             dp[i+1][j]=dp[i][j];
                             if(str2[i]==str1[j])
                             {
                                                if(j==0)dp[i+1][j]=(dp[i][j]+1)%10000;
                                                else dp[i+1][j]=(dp[i][j]+dp[i][j-1])%10000;
                             }
                    }
            }
            printf("Case #%d: %04d\n",kase,dp[l2][l1-1]);
    }
}
