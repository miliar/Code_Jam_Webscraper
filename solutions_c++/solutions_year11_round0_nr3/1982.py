#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,n,tmp;
    int cas,t,flag,min,ans;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);
        scanf("%d",&min);
        flag=min;
        ans=min;
        for(i=2;i<=n;i++)
        {
            scanf("%d",&tmp);
            if (tmp<min) min=tmp;
            flag=(flag^tmp);
            ans+=tmp;
        }
        ans-=min;
        printf("Case #%d: ",cas);
        if (flag!=0) printf("NO\n");
        else printf("%d\n",ans);
    }
    return 0;
}
