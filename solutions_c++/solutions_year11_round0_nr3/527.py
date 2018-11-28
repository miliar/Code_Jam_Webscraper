#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n,mn,a,sum,s,cases=1;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        mn=100000000;
        sum=s=0;
        for(int i=0;i<n;++i)
        {
            scanf("%d",&a);
            mn=min(mn,a);
            sum+=a;
            s^=a;
        }
        if(s)
            printf("Case #%d: NO\n",cases++);
        else
            printf("Case #%d: %d\n",cases++,sum-mn);
    }
    return 0;
}
