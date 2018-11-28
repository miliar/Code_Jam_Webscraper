#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int N,S,Q;
char sg[110][110];
int q[1010];
int dp[1010][110];

int main()
{
    //freopen("G:\\A-large.in","r",stdin);
    //freopen("G:\\A-large.out","w",stdout);
    int i,j,t=1,min;
    char temp[110];
    scanf("%d",&N);
    while(N--)
    {
        memset(dp,0,sizeof(dp));
        memset(q,0,sizeof(q));
        scanf("%d",&S);
        getchar();
        for(i=1;i<=S;i++)
        {
            fgets(sg[i],110,stdin);
            sg[i][strlen(sg[i])-1]='\0';
            //scanf("%s",sg[i]);
        }
        scanf("%d",&Q);
        if(Q==0)
        {
            printf("Case #%d: 0\n",t);
        }
        else
        {
            getchar();
            for(i=1;i<=Q;i++)
            {

                fgets(temp,110,stdin);
                temp[strlen(temp)-1]='\0';
                //scanf("%s",temp);
                for(j=1;j<=S;j++)
                {
                    if(strcmp(temp,sg[j])==0)
                    {
                        q[i]=j;
                        break;
                    }
                }
            }
            /*for(i=1;i<=S;i++)
                printf("%s\n",sg[i]);
            for(j=1;j<=Q;j++)
                printf("%d\n",q[j]);*/
            for(i=1;i<=Q;i++)
             for(j=1;j<=S;j++)
                dp[i][j]=10000;
            for(i=1;i<=Q;i++)
            {
                for(j=1;j<=S;j++)
                {
                    if(q[i]!=j)
                    {
                        if(q[i-1]!=j)
                        {
                            if(dp[i][j]>dp[i-1][j])
                                dp[i][j]=dp[i-1][j];
                        }
                        if(q[i-1]!=q[i])
                        {
                            if(dp[i][j]>dp[i-1][q[i]]+1)
                                dp[i][j]=dp[i-1][q[i]]+1;
                        }
                    }
                }
            }
            /*for(i=1;i<=Q;i++)
            {
                for(j=1;j<=S;j++)
                    printf("%d ",dp[i][j]);
                printf("\n");
            }*/
            min=10000;
            for(i=1;i<=S;i++)
                if(dp[Q][i]<min)
                    min=dp[Q][i];
            printf("Case #%d: %d\n",t,min);
        }
        t++;
    }
    return 0;
}
