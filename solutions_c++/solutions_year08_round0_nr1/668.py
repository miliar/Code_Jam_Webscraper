#include<stdio.h>
#include<string.h>
#include<string>
using namespace std;

char eng[110][110],tem[110];
bool g[1010][110];
int dp[1010][110],s,q,i,j,jj,n1,i1,Min;

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d",&s);
        gets(tem);
        for(i=1;i<=s;i++)
        {
            gets(eng[i]);
        }
        scanf("%d",&q);
        gets(tem);
        memset(g,false,sizeof(g));
        for(i=1;i<=q;i++)
        {
            gets(tem);
            for(j=1;j<=s;j++)
            {
                if(strcmp(tem,eng[j])==0)
                    g[i][j]=true;
            }
        }
        memset(dp,0,sizeof(dp));
        for(i=1;i<=q;i++)
            for(j=1;j<=s;j++)
            {
                if(g[i][j])
                    dp[i][j]=-1;
                else
                {
                    Min=2000;
                    for(jj=1;jj<=s;jj++)
                    {
                        if(dp[i-1][jj]==-1)
                            continue;
                        if(jj==j)
                        {
                            if(dp[i-1][jj]<Min)
                                Min=dp[i-1][jj];
                        }
                        else
                        {
                            if(dp[i-1][jj]+1<Min)
                                Min=dp[i-1][jj]+1;
                        }
                    }
                    dp[i][j]=Min;
                }
            }
        Min=2000;
        for(i=1;i<=s;i++)
        {
            if(dp[q][i]==-1)
                continue;
            if(dp[q][i]<Min)
                Min=dp[q][i];
        }
        printf("Case #%d: %d\n",i1,Min);
    }
    return 0;
}
