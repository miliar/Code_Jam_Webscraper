#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int v[2000];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,h=1,n;;
    scanf("%d",&t);
    while(t--)
    {
        __int64 ans=0;
        scanf("%d",&n);
        scanf("%d",&v[0]);
        int sum=v[0];
        int i;
        for(i=1;i<n;i++)
        {
            scanf("%d",&v[i]);
            sum=sum^v[i];
        }
        printf("Case #%d: ",h++);
        if(sum!=0)
        {
            printf("NO\n");
            continue;
        }
        else
        {
            sort(v,v+n);
            for(i=n-1;i>=1;i--)
            {
                ans+=v[i];
            }
            printf("%I64d\n",ans);
        }
    }
    return 0;
}
