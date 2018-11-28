#include<iostream>
using namespace std;
typedef long long LL;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int cas;
    LL l,p,c;
    scanf("%d",&cas);
    for (int T = 1; T <= cas;T++)
    {
        scanf("%lld%lld%lld",&l,&p,&c);
        LL t = (p - 1) / l + 1;
        int ans = 0;
        while (c < t)
        {
            c *= c;
            ans++;
        }
        printf("Case #%d: %d\n",T,ans);
    }
}
