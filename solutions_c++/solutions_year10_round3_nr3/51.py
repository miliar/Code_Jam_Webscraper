#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;
bool tu[513][513];
bool flag[513][513];
int ans[513];
bool check(int x1,int y1,int x2,int y2)
{
    int i,j;
    if(tu[x1][y1]==1)
    {
        for(i=x1;i<=x2;i++)
        {
            for(j=y1;j<=y2;j++)
            {
                if(flag[i][j]==0) return 0;
                if((i-x1+j-y1)%2==0&&tu[i][j]==0) return 0;
                if((i-x1+j-y1)%2==1&&tu[i][j]==1) return 0;
            }
        }
    }
    if(tu[x1][y1]==0)
    {
        for(i=x1;i<=x2;i++)
        {
            for(j=y1;j<=y2;j++)
            {
                if(flag[i][j]==0) return 0;
                if((i-x1+j-y1)%2==0&&tu[i][j]==1) return 0;
                if((i-x1+j-y1)%2==1&&tu[i][j]==0) return 0;
            }
        }        
    }
    return 1;
}
void fun(int x1,int y1,int x2,int y2)
{
    int i,j;
    for(i=x1;i<=x2;i++)
    {
        for(j=y1;j<=y2;j++)
        {
            flag[i][j]=0;
        }
    }
}
int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,i,j,k,M,N,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        cas++;
        char tt[200];
        scanf("%d%d",&M,&N);
        memset(flag,true,sizeof(flag));
        for(i=1;i<=M;i++)
        {
            scanf("%s",tt);
            for(j=1;4*j<=N;j++)
            {
                if(tt[j-1]>='0'&&tt[j-1]<='9')
                {
                    int num=tt[j-1]-'0';
                    tu[i][4*j]=num&1;num>>=1;
                    tu[i][4*j-1]=num&1;num>>=1;
                    tu[i][4*j-2]=num&1;num>>=1;
                    tu[i][4*j-3]=num&1;num>>=1;
                }
                if(tt[j-1]>='A')
                {
                    int num=tt[j-1]-'A'+10;
                    tu[i][4*j]=num&1;num>>=1;
                    tu[i][4*j-1]=num&1;num>>=1;
                    tu[i][4*j-2]=num&1;num>>=1;
                    tu[i][4*j-3]=num&1;num>>=1;
                }
            }
        }
        int L=M<N?M:N,res=0;
        memset(ans,0,sizeof(ans));
        for(k=L;k>=1;k--)
        {
            for(i=1;i+k-1<=M;i++)
            {
                for(j=1;j+k-1<=N;j++)
                {
                    if(check(i,j,i+k-1,j+k-1))
                    {
                        ans[k]++;
                        fun(i,j,i+k-1,j+k-1);
                    }
                }
            }
        }
        for(i=1;i<=L;i++)
        {
            if(ans[i]>0) res++;
        }
        printf("Case #%d: %d\n",cas,res);
        for(i=L;i>=1;i--)
        {
            if(ans[i]>0)
            {
                printf("%d %d\n",i,ans[i]);
            }
        }
    }
    return 0;
}
