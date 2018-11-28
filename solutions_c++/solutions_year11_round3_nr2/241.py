#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

__int64 l,n,c;
__int64 t;
__int64 s[1000005];
__int64 d[1000005];

int main()
{
    freopen("B-large(2).in","r",stdin);
    freopen("B-large(2).out","w",stdout);
    int q;
    int h=1;
    scanf("%d",&q);
    while(q--)
    {
        __int64 sum=0;
        int i,j;
        scanf("%I64d%I64d%I64d%I64d",&l,&t,&n,&c);
        for(i=0;i<c;i++)
        {
            scanf("%I64d",&s[i]);
        }
        for(i=0;i<n;i++)
        {
            j=i%c;
            d[i]=s[j];
            sum+=d[i]*2;
        }
        int x=0;
        for(i=0;i<n;i++)
        {
            t-=(d[i]*2);
            if(t<0)
            {
                d[i]=(-t)/2;
                x=i;
                break;
            }
        }
        sort(d+x,d+n);
        printf("Case #%d: ",h++);
        if(l>n-x)
        {
            l=n-x;
        }
        for(i=0;i<l;i++)
        {
            sum-=d[n-1-i];
        }
        printf("%I64d\n",sum);
    }
    return 0;
}
