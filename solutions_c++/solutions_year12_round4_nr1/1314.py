#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std;

const int Maxn=10010;
struct P
{
    int d,l,dd;
    bool operator < (const P &r) const
    {
        return d<r.d;
    }
} a[Maxn];
int n,d;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int T=1; T<=cas; ++T){
        scanf("%d",&n);
        for(int i=1; i<=n; ++i){
            scanf("%d%d",&a[i].d,&a[i].l);
            a[i].dd=0;
        }
        sort(a+1,a+n+1);
        scanf("%d",&d);
        a[1].dd=a[1].d;
        bool ret=0;
        for(int i=1; i<=n; ++i) {
            if(a[i].d+a[i].dd>=d) {
                ret=1;
                break;
            }
            for(int j=i+1; j<=n&&(a[j].d-a[i].d)<=a[i].dd; ++j)
                a[j].dd=max(a[j].dd,min(a[j].d-a[i].d,a[j].l));
        }
        printf("Case #%d: ",T);
        if(ret) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
