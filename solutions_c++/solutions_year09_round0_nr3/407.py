#include <stdio.h>
#include <string.h>
int main()
{
    freopen("codejam.in","r",stdin);
    freopen("codejam.out","w",stdout);
    int tc,c,i,j,l,t;
    char str[510];
    char ori[20]="welcome to code jam";
    int dp[510][20]={0};
    int prev[128][3]={0};
    prev['a'][0]=18;
    prev['c'][0]=4;
    prev['c'][1]=12;
    prev['d'][0]=14;
    prev['e'][0]=2;
    prev['e'][1]=7;
    prev['e'][2]=15;
    prev['j'][0]=17;
    prev['l'][0]=3;
    prev['m'][0]=6;
    prev['m'][1]=19;
    prev['o'][0]=5;
    prev['o'][1]=10;
    prev['o'][2]=13;
    prev['t'][0]=9;
    prev['w'][0]=1;
    prev[' '][0]=8;
    prev[' '][1]=11;
    prev[' '][2]=16;
    gets(str);
    sscanf(str,"%d",&tc);
    for(c=0;c<tc;c++)
    {
        for(i=0;i<510;i++)
            memset(dp[i],0,20*sizeof(int));
        t=0;
        gets(str);
        l=strlen(str);
        dp[0][0]=1;
        for(i=0;i<l;i++)
        {
            for(j=0;j<=i;j++)
            {
                if(prev[str[i]][0])
                {
                    dp[i+1][prev[str[i]][0]]=(dp[i+1][prev[str[i]][0]] + dp[j][prev[str[i]][0]-1])%10000;
                    if(prev[str[i]][1])
                    {
                        dp[i+1][prev[str[i]][1]]=(dp[i+1][prev[str[i]][1]] + dp[j][prev[str[i]][1]-1])%10000;
                        if(prev[str[i]][2])
                            dp[i+1][prev[str[i]][2]]=(dp[i+1][prev[str[i]][2]] + dp[j][prev[str[i]][2]-1])%10000;
                    }
                }
            }
            t += dp[i+1][19];
        }
        printf("Case #%d: %04d\n",c+1,t%10000);
    }
    return 0;
}
