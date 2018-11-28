#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tt;

int main()
{
    freopen("candy.in","r",stdin);
    freopen("candy.out","w",stdout);
    scanf("%d",&tt);
    for (int w=1;w<=tt;w++)
    {
        int min=0x7fffffff,sum=0,j=0,n,t;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&t);
            sum+=t;
            j^=t;
            if (t<min)
                min=t;
        }
        if (j==0)
            printf("Case #%d: %d\n",w,sum-min);
        else
            printf("Case #%d: NO\n",w);
    }
    return 0;
}
