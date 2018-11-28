#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int N = 1005,INF = 1<<29;
const double eps = 1e-10;
const double pi = acos(1.);
int n,m;
int x[N][N];
int t[N][N];

bool ok(int a,int  b)
{
    int i;
    for(i=0;i<m;i++)if(x[a][i]==x[b][i])return 0;
    for(i=0;i<m-1;i++)
    {
        if(x[a][i]>x[b][i]&&x[a][i+1]<x[b][i+1]||
        x[a][i]<x[b][i]&&x[a][i+1]>x[b][i+1]
        )return 0;
    }
    return 1;
}
int y[N],match[N];
bool dfs(int v)
{
    int i;
    for(i=0;i<n;i++)
        if(t[v][i]&&!y[i])
        {
            y[i]=1;
            if(match[i]==-1||dfs(match[i]))
            {
                match[i]=v;
                return 1;
            }
        }

    return 0;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,j,k;
    int T,K=1,ans;
    scanf("%d",&T);
    while(T--)
    {
        memset(t,0,sizeof(t));
        printf("Case #%d: ",K++);
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            match[i]=-1;
            for(j=0;j<m;j++)
                scanf("%d",&x[i][j]);
        }
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(ok(i,j))
                {
                    if(x[i][0]<x[j][0])t[i][j]=1;
                    else t[j][i]=1;
                }
            }
        }
//        for(i=0;i<n;i++)
//        {
//            for(j=0;j<n;j++)
//                printf("%d ",t[i][j]);puts("");
//        }
        ans = n;
        for(i=0;i<n;i++)
        {
            memset(y,0,sizeof(y));
            if(dfs(i))ans--;
        }
        printf("%d\n",ans);
    }
    return 0;
}
