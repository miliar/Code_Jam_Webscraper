#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
#define maxn 1010
#define maxm 20000
int T;
int cnt[maxn];
int flag[maxn];
int head[maxn];
int mp[maxn][maxn];
int size;
struct Edge
{
    int v,next;

    Edge() {}
    Edge(int a,int c):v(a),next(c) {}
} edge[maxm];
inline void initg()
{
    size = 0;
    memset(head,-1,sizeof(head));
}
inline void add_edge(int u,int v)
{
    edge[size] = Edge(v,head[u]);
    head[u] = size++;
}
bool DFS(int k)
{
    int i,v;
    bool jj;
    flag[k] = 1;
    for(i = head[k]; i!=-1; i = edge[i].next)
    {
        v = edge[i].v;
        if(flag[v] == 1)
            return true;
        else
        {
            jj = DFS(v);
            if(jj == true)
                return true;
        }
    }
    return false;

}
bool solve(int n)
{
    int i;

    for(i = 1; i <= n; i++)
    {

         if(cnt[i] == 0)
         {
              memset(flag,0,sizeof(flag));
            if(DFS(i))
                return true;
         }
    }
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
    int cs,n,i,k,v;
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {

            scanf("%d",&n);
            initg();
            memset(cnt,0,sizeof(cnt));
            memset(mp,0,sizeof(mp));
            for(i = 0; i < n; i++)
            {
                scanf("%d",&k);
                while(k--)
                {
                    scanf("%d",&v);
                   // if(mp[i+1][v] == 0)
                 //   {
                  //      mp[i+1][v] = 1;

                        add_edge(i+1,v);
                        cnt[v]++;
                  //  }
                }
            }
            printf("Case #%d: ",cs++);
            if(solve(n))
                printf("Yes\n");
            else
                printf("No\n");
        }
    }
    return 0;
}
