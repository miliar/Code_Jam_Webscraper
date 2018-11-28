#include <iostream>
#include <cstdio>
using namespace std;
const int N = 1001;
int a[N];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,mn = 1<<29,sum =0;
        scanf("%d",&n);
        int ans = 0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            ans^= a[i];
            mn = min(mn,a[i]);
            sum+=a[i];
        }
        if(ans )
        {
            printf("Case #%d: NO\n",cas++);
        }
        else
        {
            printf("Case #%d: %d\n",cas++,sum-mn);
        }
    }
    return 0;
}
