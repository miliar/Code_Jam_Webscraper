#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
    int n,k;
    int inp[100][25];
int is_sm(int v,int u)
{
    for(int i=0;i<k;i++)
        if(inp[v][i]>=inp[u][i])
            return false;
    return true;

}
vector<int> out[100];
vector<int> in[100];
int lm[100];
int rm[100];
int lc[100];
int rc[100];
int color;
bool rdfs(int v);
bool ldfs(int u)
{
    lc[u] = color;
    for(int i=0;i<out[u].size();i++)
    {
        int v = out[u][i];
        if(rc[v] == color)
            continue;
        if(rdfs(v))
        {
            rm[v] = u;
            lm[u] = v;
            return true;
        }
    }
    return false;
}

bool rdfs(int v)
{
    rc[v] = color;
    if(rm[v] == -1)
        return true;
    if(ldfs(rm[v]))
        return true;
    return false;
}

int tst()
{
    scanf("%d%d",&n,&k);
    for(int i=0;i<n;i++)
        for(int j=0;j<k;j++)
            scanf("%d",&inp[i][j]);
    for(int i=0;i<100;i++)
    {
        out[i].clear();
        in[i].clear();
    }
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        {
            if(is_sm(i,j))
            {
                out[i].push_back(j);
                in[j].push_back(i);
//                printf("add edge %d %d\n",i,j);
            }
        }
    for(int i=0;i<n;i++)
        lc[i] = rc[i] = lm[i] = rm[i] = -1;
    for(int i=0;i<n;i++)
        if(lm[i]==-1)
        {
            color = i;
            ldfs(i);
        }
    int ans=0;
    for(int i=0;i<n;i++)
        if(lm[i]==-1)
            ans ++;
    return ans;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        printf("Case #%d: %d\n",i,tst());
    }
}
