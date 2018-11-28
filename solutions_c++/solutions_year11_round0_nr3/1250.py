#include <stdio.h>
#include <algorithm>
int a[1010];
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        printf("Case #%d: ",ii);
        sort(a,a+n);
        int ans=0;
        for (int i=0;i<n-1;i++)
            ans=ans^a[i];
        if (ans!=a[n-1]) puts("NO");
        else
        {
            int ans=0;
            for (int i=1;i<n;i++)
                ans+=a[i];
            printf("%d\n",ans);
        }
    }
    return 0;
}
