#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int cntt=0;cntt<t;cntt++)
    {
        long long l,p,c;
        scanf("%I64d%I64d%I64d",&l,&p,&c);
        int cnt=0;
        for(long long tmp=l;;tmp=tmp*c)
        {
            cnt++;
            if(tmp>=p)
                break;
        }
        int ans=0;
        for(int q=cnt;q>2;q=q/2+1)
        {
            ans++;
        }
        printf("Case #%d: %d\n",cntt+1,ans);
    }
    return (0);
}

