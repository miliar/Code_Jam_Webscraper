#include <iostream>
#include <stdio.h>
#define inf 0x7fffffff
using namespace std;

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t,n,sum,min,now,m;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        min=inf;
        sum=0;
        scanf("%d",&n);
        for(int j=1;j<=n;j++)
        {
            if(j==1)
            {
                scanf("%d",&now);
                sum+=now;
                if(min>now) min=now;
                continue;
            }
            scanf("%d",&m);
            now=(now^m);
            sum+=m;
            if(min>m) min=m;
        }
        if(now)
        {
            printf("Case #%d: NO\n",i);
        }
        else
        {
            printf("Case #%d: %d\n",i,sum-min);
        }
    }
    return 0;
}
