#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#define Maxn 10010
using namespace std;
struct P
{
    int d,l,b;
} p[Maxn];
int n,d;
void ini()
{
    scanf("%d",&n);
    for(int i=1; i<=n; ++i)
    {
        scanf("%d%d",&p[i].d,&p[i].l);
        p[i].b=0;
    }
    scanf("%d",&d);
}
bool solve()
{
    p[1].b=p[1].d;
    bool ok=0;
    for(int i=1; i<=n; ++i)
    {
        if(p[i].d+p[i].b>=d)
        {
            ok=1;
            break;
        }
        for(int j=i+1; j<=n&&(p[j].d-p[i].d)<=p[i].b; ++j)
        {
            p[j].b=max(p[j].b,min(p[j].d-p[i].d,p[j].l));
        }
    }
    return ok;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ci=1; ci<=cas; ++ci)
    {
        ini();
        printf("Case #%d: ",ci);
        if(solve())printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
