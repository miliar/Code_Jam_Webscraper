#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;
int n,T,gg;
int d[1002];
int g[1002][1002];
bool vis[1002];
bool check(int r)
{
     memset(vis,0,sizeof(vis));
     queue<int> que;
     que.push(r);
     while (!que.empty())
     {
           int a=que.front();
           que.pop();
           if (vis[a])
              return true;
           vis[a]=true;
           for (int i=0;i<d[a];i++)
               que.push(g[a][i]);
     }
     return false;
}
int main()
{
    freopen("a2.in","r",stdin);
    freopen("a2.out","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
          scanf("%d",&n);
          for (int i=1;i<=n;i++)
          {
              scanf("%d",&d[i]);
              for (int j=0;j<d[i];j++)
                  scanf("%d",&g[i][j]);
          }
          for (int i=1;i<=n;i++)
          if (check(i))
          {
             printf("Case #%d: Yes\n",++gg);
             goto nex;
          }
          printf("Case #%d: No\n",++gg);
          nex:;
    }
}
