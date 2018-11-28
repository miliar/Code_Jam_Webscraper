#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXN 100
#define MAXK 25
using namespace std;

char graph[MAXN+1][MAXN+1];
int data[MAXN+1][MAXK+1];
char visited[MAXN+1];
int match[MAXN+1];
int n,k;

char DFS(int i)
{
    int j;
    for(j=0;j<n;j++)
    {
        if((graph[i][j]==1)&&(visited[j]==0))
        {
            visited[j]=1;
            if((match[j]==-1)||(DFS(match[j])==1))
            {
                match[j]=i;
                return 1;
            }
        }
    }
    return 0;
}

int max_match()
{
    int i,maxmatch;
    memset(match,-1,sizeof(match));
    maxmatch=0;
    for(i=0;i<n;i++)
    {
        memset(visited,0,sizeof(visited));
        if(DFS(i)==1)
        {
            maxmatch++;
        }
    }
    return maxmatch;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,l,p,t;
    scanf("%d",&t);
    for(p=0;p<t;p++)
    {
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++)
        {
            for(j=0;j<k;j++)
            {
                scanf("%d",&data[i][j]);
            }
        }
        memset(graph,0,sizeof(graph));
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i!=j)
                {
                    for(l=0;l<k;l++)
                    {
                        if(data[i][l]>=data[j][l])
                        {
                            break;
                        }
                    }
                    if(l>=k)
                    {
                        graph[i][j]=1;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",p+1,n-max_match());
    }
    return 0;
}
