#include<stdio.h>
#include<memory.h>
#include<set>
#include<map>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>
#include<iostream>
using namespace std;

int i1,n1,er[15],g[20][20],dp[11][3000],u,i,J1,j,jj,m,n,da;
char str[15];

int main()
{
    er[0]=1;
    for(i=1;i<=10;i++)
        er[i]=er[i-1]*2;
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d %d",&m,&n);
        gets(str);
        memset(g,0,sizeof(g));
        for(i=1;i<=m;i++)
        {
            gets(str);
            for(j=0;j<strlen(str);j++)
            {
                if(str[j]=='x')
                    g[i][j]=1;
            }
        }
        memset(dp,0,sizeof(dp));
        for(i=1;i<=m;i++)
        {
            for(j=0;j<er[n];j++)
            {
                     u=0;
                    for(jj=0;jj<n;jj++)
                    {
                        if(g[i][jj]==1&&(j&er[jj])!=0)
                        {
                            u=1;
                            break;
                        }
                    }
                    if(u==1)
                        continue;
                    for(jj=0;jj<n-1;jj++)
                    {
                        if((j&er[jj])!=0&&(j&er[jj+1])!=0)
                        {
                            u=1;
                            break;
                        }
                    }
                    if(u==1)
                        continue;
                for(jj=0;jj<n;jj++)
                {
                    if((j&er[jj])!=0)
                        dp[i][j]++;
                }
                if(i==m)
                    continue;
                for(J1=0;J1<er[n];J1++)
                {
                    u=0;
                    for(jj=0;jj<n;jj++)
                    {
                        if(g[i+1][jj]==1&&(J1&er[jj])!=0)
                        {
                            u=1;
                            break;
                        }
                    }
                    if(u==1)
                        continue;
                    for(jj=0;jj<n-1;jj++)
                    {
                        if((J1&er[jj])!=0&&(J1&er[jj+1])!=0)
                        {
                            u=1;
                            break;
                        }
                    }
                    if(u==1)
                        continue;
                    for(jj=0;jj<n;jj++)
                    {
                        if(jj-1>=0)
                        {
                            if((J1&er[jj])!=0&&(j&er[jj-1])!=0)
                            {
                                u=1;
                                break;
                            }
                        }
                        if(jj+1<n)
                        {
                            if((J1&er[jj])!=0&&(j&er[jj+1])!=0)
                            {
                                u=1;
                                break;
                            }
                        }
                    }
                    if(u==1)
                        continue;
                    if(dp[i][j]>dp[i+1][J1])
                        dp[i+1][J1]=dp[i][j];
                }
            }
        }
 /*     for(i=1;i<=m;i++)
            
        for(j=0;j<er[n];j++)
        {
            printf("%d %d:%d\n",i,j,dp[i][j]);
        }    */
        da=0;
        for(j=0;j<er[n];j++)
        {
            if(dp[m][j]>da)
                da=dp[m][j];
        }
        printf("Case #%d: %d\n",i1,da);
    }
    return 0;
}       
