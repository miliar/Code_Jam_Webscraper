#include <cstdio>
#include <iostream>
#include <cstring>
#include <numeric>
#define SIZE 19
#define MAXL 500
#define MOD 10000
using namespace std;

const char word[SIZE+2]="$welcome to code jam";
int dp[SIZE+2][MAXL+2];
char line[MAXL+2];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,k,t,len;
    gets(line);
    sscanf(line,"%d",&t);
    for(k=0;k<t;k++)
    {
        gets(&line[1]);
        len=strlen(&line[1]);
        memset(dp,0,sizeof(dp));
        dp[0][0]=1;
        for(i=1;i<=SIZE;i++)
        {
            for(j=i;j<=len;j++)
            {
                if(word[i]==line[j])
                {
                    dp[i][j]=accumulate(dp[i-1],dp[i-1]+j,0)%MOD;
                }
            }
        }
        printf("Case #%d: %04d\n",k+1,accumulate(dp[SIZE],dp[SIZE]+len+1,0)%MOD);
    }
    return 0;
}
