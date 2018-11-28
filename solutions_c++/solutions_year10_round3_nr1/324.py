#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int cnt=0;cnt<t;cnt++)
    {
        int a[1001],b[1001];
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&a[i],&b[i]);
        }
        int ans=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<i;j++)
            {
                if(a[i]<a[j]&&b[i]>b[j])
                    ans++;
                if(a[i]>a[j]&&b[i]<b[j])
                    ans++;
            }
            printf("Case #%d: %d\n",cnt+1,ans);
    }

    return (0);
}

