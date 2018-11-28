#include <cstdio>
#include <cstring>
static const int MAXN = 1010;
static const int MAXM = 10010;
struct Edge
{
    int v, next;
}edge[MAXM];
int edgeNumber, head[MAXN];
int in[MAXN];
int color[MAXN];

inline void addEdge(int u, int v)
{
    edge[edgeNumber].v = v;
    edge[edgeNumber].next = head[u];
    head[u] = edgeNumber ++;
}

bool dfs(int x, int c)
{
    for(int i=head[x];i!=-1;i=edge[i].next)
    {
        if(color[edge[i].v] == c)
        {
            return true;
        }
        color[edge[i].v] = c;
        if(dfs(edge[i].v, c))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int caseNumber;
    scanf("%d", &caseNumber);
    for(int cas=1;cas<=caseNumber;++cas)
    {
        edgeNumber = 0;
        memset(head, -1, sizeof(head));
        memset(in, 0, sizeof(in));
        memset(color, 0, sizeof(color));
        int n;
        scanf("%d", &n);
        for(int i=1;i<=n;++i)
        {
            int k, v;
            scanf("%d", &k);
            for(int j=0;j<k;++j)
            {
                scanf("%d", &v);
                addEdge(i, v);
                ++in[v];
            }
        }
        bool flag = false;
        for(int i=1;i<=n;++i)
        {
            if(in[i] == 0)
            {
                if(dfs(i, i))
                {
                    flag = true;
                    break;
                }
            }
        }
        printf("Case #%d: ", cas);
        if(flag) printf("Yes\n");
        else printf("No\n");
    }
    return 0;
}
