#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

struct b {
    string str;
}   baum[200010];
struct edg {
    int node,next;
}   edges[200010];
char s[200010];
int n,m,n1,top,tc,file,bt;
int g[200010];
string wort;
int add(int r, int f)
{
    if (f==n1+1) return 0;
    wort="";
    while ((f<n1) && (s[f]!='/')) wort+=s[f++];
    int p = g[r];
    while (p!=-1) {
        if (baum[edges[p].node].str == wort)
            return add(edges[p].node, f+1);
        p = edges[p].next;
    }
    baum[++bt].str = wort;
    edges[top].node = bt;
    edges[top].next = g[r];
    g[r] = top++;
    return 1+add(bt, f+1);
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tc);
    for (int t=1;t<=tc;++t)
    {
        scanf("%d%d",&n,&m);
        memset(g,-1,sizeof(g));
        top = 0;
        bt = 1;
        file = 0;
        gets(s);
        for (int i=1;i<=n;++i)
        {
            gets(s);
            n1 = strlen(s);
            add(1,1);
        }
        for (int i=1;i<=m;++i)
        {
            gets(s);
            n1 = strlen(s);
            file += add(1,1);
        }

        printf("Case #%d: %d\n",t,file);
    }
    return 0;
}
/*
*/
