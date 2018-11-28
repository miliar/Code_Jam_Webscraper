#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std;

const int Maxn=10010;
struct node
{
    int d,l,dd;
    bool operator < (const node &r) const
    {
        return d<r.d;
    }
} N[Maxn];
int n,d;

bool solve()
{
    bool ret=0;
    for(int i=1; i<=n; ++i)
    {
        if(N[i].d+N[i].dd>=d)
        {
            ret=1;
            break;
        }
        for(int j=i+1; j<=n&&(N[j].d-N[i].d)<=N[i].dd; ++j)
            N[j].dd=max(N[j].dd,min(N[j].d-N[i].d,N[j].l));
    }
    return ret;
}

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int c,k=0;
    for(scanf("%d",&c); c--; )
    {
        scanf("%d",&n);
        for(int i=1; i<=n; ++i)
            scanf("%d%d",&N[i].d,&N[i].l),N[i].dd=0;
        sort(N+1,N+n+1);
        scanf("%d",&d);
        N[1].dd=N[1].d;
        printf("Case #%d: ",++k);
        if(solve()) puts("YES");
        else puts("NO");
    }
    return 0;
}
