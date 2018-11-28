#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

long long tt;
long long l,n,c;
long long t;
long long a[1024];
long long sum[1001000];
long long d[1001000];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%I64d",&tt);
    for (long long ii=1; ii<=tt; ii++)
    {
        scanf("%I64d",&l);
        cin >> t;
        scanf("%I64d%I64d",&n,&c);
        sum[0]=0;
        for (long long i=1; i<=c; i++)
            scanf("%I64d",a+i);
        a[0]=a[c];
        for (long long i=1; i<=n; i++)
        {
            d[i]=a[i%c];
            sum[i]=sum[i-1]+d[i];
        }
        sum[n+1]=sum[n];
        d[0]=0;
        long long dist=0;
        long long p;
        long long le=0,re=n,mid;
        while (le<re)
        {
            mid=(le+re)/2;
            if (mid==n || (sum[mid]<=t/2 && sum[mid+1]>t/2))
                break;
            if (sum[mid]<=t/2)
                le=mid+1;
            else
                re=mid-1;
        }
        mid=(le+re)/2;
        p=mid;
        dist=sum[mid];
        if (d+p+2<d+n+1)
            sort(d+p+2,d+n+1);
        printf("Case #%I64d: ",ii);
        if (l>0)
        {
            if (l>=n-p)
                printf("%I64d\n",t+sum[n]-t/2);
            else
            {
                long long i,ans=sum[n]*2;
                for (i=n; l>1; i--)
                {
                    l--;
                    ans-=d[i];
                }
                if (sum[p+1]-t/2<d[i])
                    ans-=d[i];
                else
                    ans-=sum[p+1]-t/2;
                printf("%I64d\n",ans);
            }
        }
        else
            printf("%I64d\n",sum[n]*2);
    }
    return 0;
}
