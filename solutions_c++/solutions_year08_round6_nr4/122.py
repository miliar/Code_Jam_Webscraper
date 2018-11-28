#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <memory>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#define MAXN 100
using namespace std;

bool graph1[MAXN+1][MAXN+1],graph2[MAXN+1][MAXN+1];
bool used[MAXN+1];
int pos[MAXN+1];
int n,m;

bool check()
{
    int i,j;
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=m;j++)
        {
            if(graph2[i][j]!=graph1[pos[i]][pos[j]])
            {
                return false;
            }
        }
    }
    return true;
}

bool backtrack(int k)
{
    int i;
    if(k>m)
    {
        if(check()==true)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    for(i=1;i<=n;i++)
    {
        if(used[i]==false)
        {
            used[i]=true;
            pos[k]=i;
            if(backtrack(k+1)==true)
            {
                return true;
            }
            used[i]=false;
        }
    }
    return false;
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int c,i,t,x,y;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        memset(graph1,0,sizeof(graph1));
        memset(graph2,0,sizeof(graph2));
        scanf("%d",&n);
        for(i=1;i<n;i++)
        {
            scanf("%d %d",&x,&y);
            graph1[x][y]=graph1[y][x]=true;
        }
        scanf("%d",&m);
        for(i=1;i<m;i++)
        {
            scanf("%d %d",&x,&y);
            graph2[x][y]=graph2[y][x]=true;
        }
        memset(used,0,sizeof(used));
        printf("Case #%d: ",c+1);
        if(backtrack(1)==true)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
