#include <iostream>

using namespace std;

long long t,iii;
long long r,k,n,g[1005],i,j;
long long to[1005],cos[1005];
long long tmp[2005],now;
long long ans;

int main()
{
    scanf("%I64d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%I64d %I64d %I64d",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            scanf("%I64d",&g[i]);
        }
        for(i=0;i<n;i++)
        {
            tmp[i]=g[i];
            tmp[n+i]=g[i];
        }
        for(i=0;i<n;i++)
        {
            j=i-1;
            now=0;
            while(now+tmp[j+1]<=k&&j+1<i+n)
            {
                j++;
                now+=tmp[j];
            }
            cos[i]=now;
            to[i]=(j+1)%n;
        }
        ans=0;
        now=0;
        for(i=0;i<r;i++)
        {
            ans+=cos[now];
            now=to[now];
        }
        printf("Case #%I64d: %I64d\n",iii,ans);
    }
    return 0;
}
