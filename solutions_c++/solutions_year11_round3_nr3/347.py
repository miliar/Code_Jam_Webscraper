#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tt,n,low,high;
int a[16384];

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tt);
    for (int ii=1;ii<=tt;ii++)
    {
        scanf("%d%d%d",&n,&low,&high);
        for (int i=1;i<=n;i++)
            scanf("%d",a+i);
        int te=0;
        for (int i=low;i<=high && te==0;i++)
        {
            bool flag=true;
            for (int j=1;j<=n;j++)
                if (!(i % a[j]==0 || a[j] % i==0))
                {
                    flag=false;
                    break;
                }
            if (flag)
            {
                te=i;
                break;
            }
        }
        printf("Case #%d: ",ii);
        if (te==0)
            puts("NO");
        else
            printf("%d\n",te);
    }
    return 0;
}
